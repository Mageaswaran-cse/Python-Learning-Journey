sub1=int(input("Enter subject1 mark:"))
sub2=int(input("Enter subject2 mark:"))
sub3=int(input("Enter subject3 mark:"))
sub4=int(input("Enter subject4 mark:"))
sub5=int(input("Enter subject5 mark:"))

total=[sub1,sub2,sub3,sub4,sub5]

sub=["sub1","sub2","sub3","sub4","sub5"]
for n in range(len(total)):
    if total[n]<45:
        print("you failed in ",sub[n])
        
average=sum(total)/len(total)
print("The average mark =",average)
