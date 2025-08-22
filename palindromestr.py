str=str(input("enter the string"))
original=str
reverse=""
for i in str:
     reverse=str[::-1]
print(reverse)
if(original==reverse):
      print("palindrome")
else:
     print("not a palindrome")

