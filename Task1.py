def calculate_area(length,width):
    if length==width:
        return "This is a square!"
    else:
        return length*width


#Inputs from the user
length=int(input("Enter the length: "))
width=int(input("Enter the width: "))
print(calculate_area(length,width))
    
