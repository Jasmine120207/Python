str=str(input("enter the string:"))
l=str.split()
print(l)
for i in l:
    count=0
    for j in i:
        count+=1
    print(count)
    if((count)%2==0):
         print(i)
    else:
        print("no even length")
   

