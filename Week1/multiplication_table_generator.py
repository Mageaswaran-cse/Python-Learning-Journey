a=int(input("Enter the Multiplication table you want:"))
b=int(input("Enter the lenght of the table:"))
print(f"\n Multiplication Table for {a} \n")
for i in range(1,b+1):
    ans=a*i
    print(f"{a}x{i}= {ans}")
