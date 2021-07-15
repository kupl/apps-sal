N=int(input())
A = list(map(int, input().split()))
A.sort()
min=0
for i in range(1,N-2):
    if (A[i+2]<A[i]+A[i+1]):
        min=i
if (min==0):
    if (A[2]<A[0]+A[1]):
        value="YES"
    else:
        value="NO"
else:
    value="YES"
if(value=="YES"):
    print(value)
    print(str(A[min+2])+" "+str(A[min+1])+" "+str(A[min]))
else:
    print(value)

