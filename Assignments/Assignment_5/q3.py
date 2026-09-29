def check_number(number):   #def check_number
    if number % 2 == 0 :    #if variable is divisible by 2
        print(f"{number} is an even number.")   #print even statement
    else :  #otherwise
        print(f"{number} is an odd number.")    #print odd statement
    
user_number = input("Enter a whole number: ")   #ask user for input

check_number(int(user_number)) #run check_number with user inputted number
