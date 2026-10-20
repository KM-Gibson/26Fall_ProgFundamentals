# Write a program that creates a database named StudentRecords.db with a table named StudentRecords. The table has the columns ID, Name, Age, and Major. The program must do the following, in this order:
# New: connect, create/open, cursor, DROP TABLE, CREATE TABLE, PRIMARY KEY
import sqlite3
# opens StudentRecords.db, or creates it
conn = sqlite3.connect("StudentRecords.db")
# the cursor runs SQL commands 
cur = conn.cursor() 

#Remove any existing StudentRecords table, then create the table.
cur.execute("DROP TABLE IF EXISTS StudentRecords")

cur.execute("""
CREATE TABLE StudentRecords (
    id INT,
    name VARCHAR(50),
    age INT,
    major VARCHAR(30),
    PRIMARY KEY (id) )
""")

# Add 5 students to the table with fixed values written in the program.
StudentRecords = [
    (1, 'Anne', 24, 'History'),
    (2, 'Bill', 22, 'Science'),
    (3, 'Chuck', 21, 'Math'),
    (4, 'Dana', 23, 'English'),
    (5, 'Eve', 25, 'Art'),
]

cur.executemany("INSERT INTO StudentRecords VALUES (?, ?, ?, ?)", StudentRecords)

# Print each student's name, age, and major. Do not print the ID.
cur.execute("SELECT name, age, major FROM StudentRecords")
for row in cur.fetchall():
    print(row)

# Ask the user: Do you want to add a new student? (yes/no). Accept yes or no in any capitalization, 

answer = input("Do you want to add a new student? (yes/no): ").lower()

if answer == "no":
    print("Okay.")

# If the user answers yes, ask for the new student's name, age, and major, one question at a time. Age must be a whole number. Name and major cannot be empty. Ask again for any invalid answer.
elif answer == "yes":
    new_name = input("What is the new student's name? ")
    new_age = int(input("What is the new student's age? "))
    new_major = input("What is the new student's major? ")
    

# Insert the new student using a query with ? placeholders. Give the new student an ID that is not already in use.
    cur.execute("INSERT INTO StudentRecords VALUES (?, ?, ?, ?)", (6, new_name, new_age, new_major))


#and ask again if the answer not yes/no
else:
    answer =input("Invalid choice. Please choose yes or no. ").lower()
    if answer == "no":
        print("Okay.")
    elif answer == "yes":
        new_name = input("What is the new student's name? ")
        new_age = int(input("What is the new student's age? "))
        new_major = input("What is the new student's major? ")
        cur.execute("INSERT INTO StudentRecords VALUES (?, ?, ?, ?)", (6, new_name, new_age, new_major))

# Commit the changes and close the database connection before the program ends.

conn.close()
