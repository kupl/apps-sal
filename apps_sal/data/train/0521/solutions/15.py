import math
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    p,q=map(int,input().split())
    k=[]
    for i in range(n):
        if p==arr[i]:
            k.append(0)
        else:
            k.append(math.atan((p-arr[i])/q))
    k=sorted(k)        
    print(round(abs(sum(k[:n//2])-sum(k[n//2:])),12))

