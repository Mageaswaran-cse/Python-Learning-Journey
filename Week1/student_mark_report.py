name=input("Enter your name:")

if not name.isalpha():
    print("Please enter your name correctly:")
    quit()

marks=[]

for i in range(1,5+1):
    mark=int(input(f"Enter the Subject{i} mark:"))

    if mark<0 or mark>100:
        Print("Enter the mark between 0 to 100. Try again")
        break

    marks.append(mark)

total_mark=sum(marks)
average=sum(marks)/len(marks)

print(f"\n Hi {name} your Mark report")

print(f"\nTotal Mark={total_mark}")
print(f"Your highest mark= {max(marks)}")
print(f"Your lowest mark= {min(marks)}\n")

print(f"Average Mark= {average}")

if average<40:
    print(f"\nYou Failed - work hard to see better result")
else:
    print(f"\nYou Passed - keep it up ")
                         
