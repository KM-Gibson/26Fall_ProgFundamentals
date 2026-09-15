item = "brand new laptop"
unit = 25.25
q = 2
tax_rate = 0.05
subtotal = unit * q
tax = subtotal * tax_rate
total = subtotal + tax
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax Amount: ${tax:.2f}")
print(f"Total: ${total:.2f}")
