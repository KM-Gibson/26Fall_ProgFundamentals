def hello(name):
    print(f"Hello {name}")

hello("Nick")
hello("Sara")
hello("John")

def add_numbers(num1, num2):
    print(num1 + num2)

add_numbers(4, 8)
add_numbers(3, 7)

def dog_info(age, name):
    print(f"Hi, my name is {name} and I am {age} years old")

dog_info(4, "Sara")

def double(number):
    return number * 2

print(double(5))
new_number = double(5)
print(new_number)


def uppercase(text):
    return text.upper()

names = ["Nick", "Jane", "Sara"]

for name in names:
    print(uppercase(name))
