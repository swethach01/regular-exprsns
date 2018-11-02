n=int(input("enter number:"))
count=0
for x in range(1,n):
    if(n%x==0):
        count=count+1
if(count>2):
    print("not prime number")
else:
    print("prime")