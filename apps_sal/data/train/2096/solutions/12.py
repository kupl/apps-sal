MOD = 1000000007
ii = lambda : int(input())
si = lambda : input()
dgl = lambda : list(map(int, input()))
f = lambda : map(int, input().split())
il = lambda : list(map(int, input().split()))
ls = lambda : list(input())
n=ii()
l=il()
l2=sorted(l)
sd=dict((l2[i],i) for i in range(n))
ans=[]
lvis=set()
for i in range(n):
    if not l[i] in lvis:
        tmp=[i+1]
        x=sd[l[i]]
        lvis.add(l[i])
        while x!=i:
            lvis.add(l[x])
            tmp.append(x+1)
            x=sd[l[x]]
        ans.append(tmp)
print(len(ans))
for i in ans:
    print(len(i),*i)
