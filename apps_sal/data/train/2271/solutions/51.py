n,m=map(int,input().split())
*p,=map(int,input().split())
p=[z-1 for z in p]
es=[[] for _ in range(n)]
for _ in range(m):
    x,y=map(int,input().split())
    es[x-1].append(y-1)
    es[y-1].append(x-1)

group=[-1]*n
last=-1
for i in range(n):
    if group[i]==-1:
        last+=1
        group[i]=last
        stack=[i]
        while stack:
            j=stack.pop()
            for e in es[j]:
                if group[e]==-1:
                    stack.append(e)
                    group[e]=last
groupset=set(group)
group1=[[] for g in groupset]
group2=[[] for g in groupset]

for i in range(n):
    group1[group[i]].append(i)
    group2[group[i]].append(p[i])

ans=0
for g in groupset:
    ans+=len(set(group1[g])&set(group2[g]))
print(ans)
