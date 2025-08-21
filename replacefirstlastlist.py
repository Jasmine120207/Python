l=[]
n=int(input("enter the size"))
for i in range(n):
  ele=int(input("enter the elements"))
  l.append(ele)
print(l)
l[0],l[-1]=l[-1],l[0]
print(l)
