# Program to find product of digit of a given no.
i=int(input("enter a no."))
product=1
while(i>0):
    product=product*(i%10)
    i=i//10
print("product of digits of a no.=",product)
