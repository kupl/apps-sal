n,k=list(map(int,input().split()))
a=[]
for _ in range(n):
    a.append(int(input()))
a.sort()
hmin=a[0]
hmax=a[k-1]
d=hmax-hmin
for i in range(0,len(a)-k):
    if(d>a[k+i-1]-a[i]):
        d=a[k+i-1]-a[i]
print(d)
