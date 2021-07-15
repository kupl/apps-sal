import collections
r=0;a,b,c=[collections.Counter() for _ in [0,0,0]]
for _ in range(int(input())):
    x,y=map(int, input().split())
    r+=a[x]+b[y]-c[(x,y)]
    a[x]+=1;b[y]+=1;c[(x,y)]+=1
print(r)
