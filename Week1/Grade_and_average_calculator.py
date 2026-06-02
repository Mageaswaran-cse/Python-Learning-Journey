name=(input("Enter your name:"))

if len(name)<3 or len(name)>12 or not name.isalpha():
    print("Name must be greater than 3 and less than 12 character and only letters. Try again...")
    quit()
    
sub1=int(input("Enter subject1 mark:"))
sub2=int(input("Enter subject2 mark:"))
sub3=int(input("Enter subject3 mark:"))
sub4=int(input("Enter subject4 mark:"))
sub5=int(input("Enter subject5 mark:"))
sub6=int(input("Enter subject6 mark:"))

Mark=[sub1,sub2,sub3,sub4,sub5,sub6]
Subject=["subject1","subject2","subject3","subject4","subject5","subject6"]

average=sum(Mark)/len(Subject)
n=average

print(f"Hi {name}!")

for a in range(len(Mark)):
    if Mark[a]<0 or Mark[a]>100:
        print(f"Mark must between 0 to 100")
        exit()
        

for a in range(len(Mark)):
    if Mark[a]<45:
        print(f"you failed in {Subject[a]}")


if sub1<45 or sub2<45 or sub3<45 or sub4<45 or sub5<45 or sub6<45:
    print('Work hard to see better result')
    exit()
else:
    print("you pass in all subject keep it up")
    
if n>=90:
    print("Grade A+")
elif n>=75:
    print("Grade A")
elif n>=65:
    print("Grade B+")
elif n>=55:
    print("Grade B")
elif n>=45:
    print("Grade C")
else :
    print("Grade U")

print(f"Your average mark= {average}")



