def add(a,b):
    return a+b
    
def subtract(a,b):
    return a-b
    
def multiply(a,b):
    return a*b
    
def divide(a,b):
    return a/b

print("----Select the operation----\n 1.Add \n 2.Subtract \n 3.Multiply \n 4.Divide")

choice=int(input("Enter your choice(1/2/3/4):"))

a=int(input("Enter the num1 ="))
b=int(input("Enter the num2 ="))

if choice==1:
    print("Result:",add(a,b))
elif choice==2:
    print("Result:",subtract(a,b))
elif choice==3:
    print("Result:",multiply(a,b))
elif choice==4:
    print("Result:",divide(a,b))
else:
    print("Invalid choice")
