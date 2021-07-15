# cook your dish here
from collections import defaultdict
from operator import itemgetter
from collections import deque

def visit(v):
    height[v][1]=0
    i=0
    coda=deque()
    coda.append(v)
    while len(coda)>0:
        num=len(coda)
        i+=1
        for _ in range(num):
            u=coda.popleft()
            for son in sons[u]:
                height[son][1]=i
                coda.append(son)
    return 

inp=list(map(int, input().split()))
n=inp[0]
wealth=inp[1:n+1]
father=[i-1 if i>0 else i for i in inp[n+1:]]
sons=defaultdict(lambda:[])
for i in range(n):
    if father[i]!=-1:
        sons[father[i]].append(i)
    else:
        boss=i

height=[[i,0] for i in range(n)]
visit(boss)

height.sort(key=itemgetter(1), reverse=True)
minimi=[0]*n
diff=[0]*n

for el in height:
    v=el[0]
    if len(sons[v])==0:
        minimi[v]=wealth[v]
        diff[v]=-float('Inf')
    else:
        minimo=min([minimi[u] for u in sons[v]]) 
        minimi[v]=min(minimo, wealth[v])
        diff[v]=max(max([diff[u] for u in sons[v]]), wealth[v]-minimo)

print(diff[boss])
    

