# Palindrom No.
i= int(input("Enter a No."))
rev=0
x=i
while(i>0):
    rev=(rev*10)+i%10
    i=i//10
if(x==rev):
    print("Palindrome No.")
else:
    print("Not Palidrome No.")
