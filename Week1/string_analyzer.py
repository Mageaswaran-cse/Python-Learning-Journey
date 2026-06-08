text = input("Enter the word or sentence:")

print(f"\nUppercase Version = {text.upper()}")
print(f"\nLowercase Version = {text.lower()}")
print(f"\nLength of String = {len(text)}")

reverse=text[::-1]
print(f"\nReverse String = {reverse}")

if text == reverse:
    print(f"\nyes it is palindrom")
else:
    print(f"\nno it is not palindrom")

    
vowels="aeiouAEIOU"
count=0
for i in text:
    if i in vowels:
        count+=1

print(f"\nVowels = {count}")
    

