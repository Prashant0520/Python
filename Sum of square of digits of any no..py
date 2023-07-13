# Program to find sum of square of digits of a given no.
i=int(input("Enter a no."))
sum=0
while(i>0):
    sum=sum+(i%10)*(i%10)
    i=i//10
print("sum of square of each digits=",sum)
