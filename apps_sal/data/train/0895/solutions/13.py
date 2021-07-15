n=int(input())
l=list(map(int,input().split()))
d=l.copy()
d.append(0)
c=d[0]
for i in range(3,n+1):
    mini=min(d[i-1],d[i-2])
    d[i]+=mini
print(c+d[-1])
