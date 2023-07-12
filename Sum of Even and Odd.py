# Sum of Even no.
n= int(input("Enter no.upto you want a sum"))
i=1
sum=0
while(i<=n):
    if(i%2==0):
        sum=sum+i
    i=i+1
print("sum of even no.",sum)

# Sum of Odd no.
n= int(input("Enter no.upto you want a sum"))
i=1
sum=0
while(i<=n):
    if(i%2!=0):
        sum=sum+i
    i=i+2
print("sum of odd no.",sum)
