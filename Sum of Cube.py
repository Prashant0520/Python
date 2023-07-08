# Program to find Sum of cube from [1-n]
n=int(input("Enter a no."))
i=1
sum=0
while(i<=n):
    sum=sum+(i*i*i)
    i=i+1
print("sum of cube=",sum)
