name=input("Enter your name:")
principal_amount=int(input("Enter the amount:"))
intrest=int(input("Enter the intrest rate:"))
month=int(input("Enter the month:"))

n=(principal_amount*intrest*month/12)/100

total=principal_amount+n
print("Hi",name)
print("The intrest price for",month,"month=",n)
print("The total amount=",total)