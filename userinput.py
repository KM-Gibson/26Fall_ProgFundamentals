user_text = input("Enter some text: ")
print(user_text)
print(user_text.upper())
user_number = input("What do you want to double? ")
print((user_number) * 2)
print(int(user_number) * 2)
user_text2 = input("Enter some text: ")
upper_or_lower = input("Type 1 for upper, 2 for lower: ")
if upper_or_lower == "1":
    print(user_text2.upper())
else:
    print(user_text2.lower())