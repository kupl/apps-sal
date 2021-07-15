from itertools import accumulate 
n=int(input())
a=tuple(map(int,input().split()))
b=tuple(accumulate(map(int,input().split())))
ssum=0
for i in range(0,n):
    for j in range(i,n):
        if i==j:
            flag=a[i]
        else:
            if i==0:
                flag=a[i]+a[j]+max(b[j-1]-b[i],b[n-1]-b[j])
            else:
                flag=a[i]+a[j]+max(b[j-1]-b[i],b[n-1]-b[j]+b[i-1])
        ssum=max(ssum,flag)
print(ssum)
