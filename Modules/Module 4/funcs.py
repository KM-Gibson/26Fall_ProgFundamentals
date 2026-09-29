def printDetails():
   print(f"Hello the name is: Alice")
   a = 2
   b = 5
   c = a*b
   print (f"The multiplication is: {c}")

printDetails() # Function Call

def printDetails2(customer_name): #define function with parameters
   print(f"Hello the name is: {customer_name}") #Variable f string
   print(f"{customer_name} is a Gold Rewards Member")
   a = 2
   b = 5
   c = a*b
   print (f"The multiplication is: {c}")

printDetails2("Alice") # Function Call with variable
printDetails2("Bob") # Function Call with variable

def Multiply_Two_Numbers(a, b): #define function with parameters
#   a = 2
#   b = 5
   c = a*b
   return c

returned_C = Multiply_Two_Numbers(2, 3) 

print (returned_C)

returned_C = Multiply_Two_Numbers(5, 3) 

print (returned_C)
