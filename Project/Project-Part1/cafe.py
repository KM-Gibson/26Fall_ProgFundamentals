cafe_name = "Python Café"
tax_rate = 0.08

menu = {
    "espresso": 3.00,
    "latte": 4.50,
    "cappuccino": 4.25,
    "mocha": 5.00,
    "muffin": 2.50,
    "croissant": 3.25,
}

order = []

#greet function
#PRINTS a welcome message with the café name and the customer's name, using an f-string.
def greet(name):
    print(f"Welcome to Python Café, {name}!")   

#show menu function
#Loops through menu.items() and PRINTS every item with its price.
def show_menu(menu):
    print("Menu:")
    for item, price in menu.items():
        print(f"  {item}: ${price:.2f}")

#show order function
#If the order is empty, prints "Your order is empty." Otherwise prints each item with its price, then the number of items using len().
def show_order(order, menu):
    if not order:
        print("Your order is empty.")
    else:
        print("Your order:")
        for item in order:
            print(f"  {item}: ${menu[item]:.2f}")
        print(f"Total items: {len(order)}")

#calculate subtotal function
#Loops through the order, adds up each item's price from the menu, and RETURNS the total.
def calculate_subtotal(order, menu):
    total = 0
    for item in order:
        total += menu[item]
    return total

#get discount function
#RETURNS the discount in dollars, using the discount rules
#Build get_discount() with one if / elif / else chain, checking the rules in this order.
#Rewards member, $20 or more, 15%
#Rewards member, $10 to under $20, 10%
#Not a member, $25 or more, 5%
#Everyone else, Any, 0%
def get_discount(subtotal, is_member):
    if is_member and subtotal >= 20:
        return subtotal * 0.15
    elif is_member and subtotal >= 10:
        return subtotal * 0.10
    elif not is_member and subtotal >= 25:
        return subtotal * 0.05
    else:
        return 0
    
#print receipt function
#Calls calculate_subtotal() and get_discount(), works out tax and the total, and PRINTS the receipt.
def print_receipt(name, order, menu, is_member):
    subtotal = calculate_subtotal(order, menu)
    discount = get_discount(subtotal, is_member)
    tax = (subtotal - discount) * tax_rate
    total = subtotal - discount + tax

    print(f"--- {cafe_name}  ---")
    print(f"Customer: {name}")
    for item in order:
        print(f"{item}: ${menu[item]:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    if is_member:
        print(f"Discount: -${discount:.2f}")
        print(f"Tax: ${tax:.2f}")
        print(f"Total: ${total:.2f}")
    if not is_member:
        print(f"Discount: -${discount:.2f}")
        print(f"Tax: ${tax:.2f}")
        print(f"Total: ${total:.2f}")
        print("Join our rewards program for more savings!")
    print(f"Thank you for your order, {name}!")


#1. Print a welcome banner that includes cafe_name.
print(f"***{cafe_name}***")

#2. Ask for the customer's name with input(), then call greet(name).
CustomerName = input("What's your name? ")
greet(CustomerName)

#3. Ask "Are you a rewards member? (yes/no)". Use .lower() and store a boolean called is_member that is True only if they typed "yes".
rewards_member = input("Are you a rewards member? (yes/no)")
def is_member():
    if rewards_member.lower() == "yes":
        return True
    else:
        return False

#4. Start a while True Each time through, print the five options below, ask the customer to choose one, and respond with if / elif / else.
while True:
    print("Please choose an option:")
    print("1. Show menu")
    print("2. Add an item")
    print("3. Remove an item")
    print("4. View my order")
    print("5. Checkout")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        #Call show_menu(menu).
        show_menu(menu)
    elif choice == "2":
        #Ask for the item and apply .lower(). If it is in menu, ask "How many?" and convert the answer with int(). If the quantity is at least 1, use a for loop with range() to append the item that many times, then confirm with an f-string. If the quantity is 0 or less, print an error. If the item isn't on the menu, say so.
        item = input("Which item would you like to add? ").lower()
        if item in menu:
            quantity = int(input("How many? "))
            if quantity > 0:
                for _ in range(quantity):
                    order.append(item)
                print(f"{quantity} {item}(s) have been added to your order.")
            else:
                print("Quantity must be at least 1.")
        else:
            print(f"{item} is not on the menu.")
    elif choice == "3":
        #Ask which item and apply .lower(). If it is in order, remove one with .remove() and confirm. Otherwise, say it isn't in the order.
        item = input("Which item? ").lower()
        if item in order:
            order.remove(item)
            print(f"{item} has been removed from your order.")
        else:
            print(f"{item} is not in your order.")
    elif choice == "4":
        #Call show_order(order, menu).
        show_order(order, menu)
    elif choice == "5":
        # If the order is empty, tell the customer to add something first and keep the loop going. Otherwise, call print_receipt(name, order, menu, is_member) and break.
        if not order:
            print("Your order is empty. Please add some items first.")
        else:
            print_receipt(CustomerName, order, menu, is_member())
            break
    else:
        print("Invalid choice. Please try again.")
