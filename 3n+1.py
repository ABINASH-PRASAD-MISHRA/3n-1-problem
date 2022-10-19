n = int(input())
i=1
print(n,end=" ")
while (n!=1):
    if(n%2==0):
        n=int(n)/2
        i=i+1
        print(int(n),end=" ")
    else: 
        n = (3*n)+1
        i=i+1
        print(int(n),end=" ")

print("",end="\n")
print("i=",i,end="\n")
