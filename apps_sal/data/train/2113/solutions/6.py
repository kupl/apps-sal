n=int(input().strip())
p=[0]+list(map(int,input().split()))

c=[0]*(n+1)
def lowbit(x):
    return x&(-x)
def add(x,v):
    while x<=n:
        c[x]+=v
        x+=lowbit(x)
def get(x):
    ans=0
    while x:
        ans+=c[x]
        x-=lowbit(x)
    return ans

ans=0
for i in range(n,0,-1):
    ans+=get(p[i])
    add(p[i],1)

if ans%2:
    print(2*ans-1)
else:
    print(2*ans)

