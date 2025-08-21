n=int(input("enter the number"))
fib=0
fib1=1
for i in range(1,n+1):
  fib2=fib+fib1
  fib1=fib
  fib2=fib1
print(fib,fib1,fib2)
