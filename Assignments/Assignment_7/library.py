# New: connect, cursor, DROP TABLE, CREATE TABLE, NOT NULL, PRIMARY KEY
import sqlite3
# opens library.db, or creates it
conn = sqlite3.connect("library.db")
# the cursor runs SQL commands 
cur = conn.cursor() 

# Remove any existing books table first, so the program can run again.
cur.execute("DROP TABLE IF EXISTS books")

# Create a table named books with these columns: id (whole number, primary key), title (text, required), author (text, required), year (whole number), genre (text), copies (whole number), and rating (whole number, may be empty).
cur.execute("""
CREATE TABLE books (
    id INT,
    title VARCHAR(50) NOT NULL,
    author VARCHAR(30) NOT NULL,
    year INT,
    genre VARCHAR(10),
    copies INT,
    rating INT,
    PRIMARY KEY (id) )
""")

# Add at least 8 books. Use at least 3 different genres and include at least 2 books with no rating. Add one book with a single INSERT statement, and add the rest with a list of tuples and executemany using ? placeholders.

cur.execute("INSERT INTO books VALUES (1, 'The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Fiction', 3, 5)")

books = [
    (2, 'To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction', 5, 5),
    (3, '1984', 'George Orwell', 1949, 'Fiction', 2, 4),
    (4, 'A Brief History of Time', 'Stephen Hawking', 1988, 'Science', 4, None),
    (5, 'The Selfish Gene', 'Richard Dawkins', 1976, 'Science', 3, 5),
    (6, 'The Art of War', 'Sun Tzu', 500, 'History', 1, None),
    (7, 'The Diary of a Young Girl', 'Anne Frank', 1947, 'History', 2, 5),
    (8, 'The Da Vinci Code', 'Dan Brown', 2003, 'Mystery', 6, 4)
]

cur.executemany("INSERT INTO books VALUES (?, ?, ?, ?, ?, ?, ?)", books)

# Print the title and author of books published after 1990.

print("\nBooks published after 1990:")
cur.execute("SELECT title, author FROM books WHERE year > 1990")
for row in cur.fetchall():
    print(row)

# Print the title of fiction books with more than 2 copies (AND).

print("\nAND: Fiction books with more than 2 copies:")
cur.execute("SELECT title FROM books WHERE genre = 'Fiction' and copies > 2")
for row in cur.fetchall():
    print(row)
# Print the title of books published before 1900 or rated 5 (OR).

print("\nOR: Books published before 1900 or rated 5:")
cur.execute("SELECT title FROM books WHERE year < 1900 OR rating = 5")
for row in cur.fetchall():
    print(row)

# Print the title of books that are not in the Mystery genre (NOT).

print("\nNOT: Books that are not Mysteries:")
cur.execute("SELECT title FROM books WHERE genre IS NOT 'Mystery'")
for row in cur.fetchall():
    print(row)
    
# Print the title of books in either the Science or History genre (IN).

print("\nIN:Books that are either Science or History.")
cur.execute("SELECT title FROM books WHERE genre IN ('Science', 'History')")
for row in cur.fetchall():
    print(row)

# Ask the user for a letter, then print the authors whose names start with that letter (LIKE). Pass the letter with a ? placeholder.

user_letter = input("Enter a letter: ")
print(f"\nLIKE: Authors that start with {user_letter}:")
cur.execute("SELECT author FROM books WHERE author LIKE ?", (user_letter + '%',))
for row in cur.fetchall():
    print(row)

# Print the title of books that have no rating (IS NULL).

print("\nNOT NULL: Books that have no rating:")
cur.execute("SELECT title FROM books WHERE rating IS NULL")
for row in cur.fetchall():
    print(row)
    
# Print a label before each result, then close the database connection.

conn.close()

