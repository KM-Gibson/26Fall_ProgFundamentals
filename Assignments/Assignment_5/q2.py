def rectangle_stats(length, width):  #define function with two parameters
    area = length * width #calculate area
    perimeter = length + width * 2 #calculate perimeter
    return area, perimeter #return parameters
    
user_length = int(input("What is the length of the rectangle? ")) #User inputs length and converts to interger
user_width = int(input("What is the width of the rectangle? ")) #User inputs length and converts to interger

rectangle_stats(user_length, user_width) #run function

rect_area, rect_perimeter = rectangle_stats(user_length, user_width) #define perimeters

print(f"The area is {rect_area:.2f}") #print area
print(f"The perimeter is {rect_perimeter:.2f}") #print perimeter
