a=int(input("enter side1"))
b=int(input("enter side2"))
c=int(input("enter side3"))
if(a>0 and b>0 and c>0):
   if(a+b>c and b+c>a and c+a>b):
      print("the given is a traingle")
else:
   print("not a traingle")
