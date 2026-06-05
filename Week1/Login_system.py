username="admin"
password="1234"
attempt=3

while attempt>0:
    user=input("Enter the Username:")
    passkey=input("Enter the Password:")
      
    if user!=username or passkey!=password:
        attempt-=1 
        print("\nLogin failed.")
        print(f"{attempt} attempt left\n")
    
    else:
        print("\nLogin Successfully\n")
        break
    
if attempt==0:
    print("\nAccount locked.Try again after 24Hrs\n")
    
