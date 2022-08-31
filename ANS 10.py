print("Enter the three numbers")
x,y,z=int(input()),int(input()),int(input())
if x>y and x>z:
    print(x,"is grater number among the three numbers.")
elif y>x and y>z:
    print(y,"is grater number among the three numbers.")
elif z>x and z>y:
    print(z,"is grater number among the three numbers.")
else:
    print("The three numbers are same equivalent.")
    
