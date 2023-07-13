# Program to find a sum of digits of a given no.
i=int(input("Enter a Given number"))
sum=0
while(i>0):
    sum=sum+i%10
    i=i//10
print("sum of digits=",sum)
