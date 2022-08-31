x=int(input("Enter the Year:"))
if x%400==0:
     print("%d is leapyear."%x)
elif x%4==0:
    print("%d is leapyear."%x)
elif x%100!=0:
    print("%d is not leapyear."%x)
else:
    print("Invalid choice.")
