pc=0
nc=0
for x in range(10):
    n=int(input("enter a number:"))
    if(n>=0):
        pc=pc+1
    else:
        nc=nc+1
print("pc=",pc)
print("nc",nc)