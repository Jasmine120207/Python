n=int(input("enter number"))
rev=0
original=n
while(n>0):
   rem=n%10
   rev=rev*10+rem
   n=n//10
print(rev)
if(rev==original):
   print("palindrome")
else:
   print("not a palindrome")
