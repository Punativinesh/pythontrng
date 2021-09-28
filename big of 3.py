x=int(input("enter number1"))
y=int(input("enter number2"))
z=int(input("enter number3"))
if(x>=y) and (x>=z):
    large=x
elif(y>=z) and (y>=x):
    large=y
else:
    large=z
print("the largest number is", large)
