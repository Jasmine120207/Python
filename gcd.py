def gcd(a,b):
    if(b==0):
       return a
    else:
       return gcd(b,a%b)
a=int(input("enter the number:"))
b=int(input("enter the number:"))
print("The gcd of numbers is :" ,gcd(a,b))
