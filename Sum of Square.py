#Program to find sum of square from [1-n]
n=int(input("Enter a no."))
i=1
sum=0
while(i<=n):
    sum=sum+(i*i)
    i=i+1
print("Sum of Square=",sum)

# Program to find sum of square from [n-1]
n=int(input("Enter a no."))
sum=0
while(n>=1):
    sum=sum+(n*n)
    n=n-1
print("Sum of Square=",sum)
