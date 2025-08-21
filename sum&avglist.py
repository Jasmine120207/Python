l=[]
n=int(input("enter size"))
for i in range(n):
  ele=int(input("enter element"))
  l.append(ele)
print(l)
sum=0
for i in l:
  sum=sum+i
print(sum)
print("the average is",sum/n)
