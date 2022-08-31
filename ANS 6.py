x=int(input("Enter the number:"))
y,s,count=x,0,0
while y:
    r=y%10
    count+=1
    y//=10
print ("The number is 3 digits number." if count==3 else "The number is not a 3 digits number.")    
