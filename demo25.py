ec=0
oc=0
for x in range(10):
    n=int(input("enter a number:"))
    if(n%2==0):
        ec=ec+1
    else:
        oc=oc+1
print("ec=",ec)
print("oc=",oc)