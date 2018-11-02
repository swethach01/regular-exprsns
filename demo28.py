pc=0
for x in range(10):
n=int(input("enter a number:"))
count=0
    for y in range(1,n):
        if(n%y==0):
            count=count+1
 if(count==2):
    pc=pc+1
print("pc=",pc)
