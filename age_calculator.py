from datetime import date
    
DOB=input("Enter your DOB(DD,MM,YY):")
day,month,year=map(int,DOB.split(","))
today=date.today()

age=today.year-year

if (today.month,today.day)<(month,day):
        age=age-1
print("Your age is",age)