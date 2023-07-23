# Sum of Even Digits and Product of Odd Digits

i=int(input("Enter a no."))
sum=0
product=1
while(i>0):
    d=i%10
    if d%2==0:
        sum=sum+d
    else:
        product=product*(i%10)
    i=i//10
print("sum of even digit=",sum,"Product of odd digit=",product)
    
