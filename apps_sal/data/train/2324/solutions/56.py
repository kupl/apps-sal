#Snuke vs Fennec
N = int(input())
tree = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = list(map(int, input().split()))
    a-=1
    b-=1
    tree[a].append(b)
    tree[b].append(a)
 
 
def dist(n, lis):
    lis[n] = 0
    node = [n]
    while node:
        s = node.pop()
        d = lis[s]
        for t in tree[s]:
            if lis[t] != -1:
                continue
            lis[t] = d + 1
            node.append(t)
    return lis
 
 
from_feneck = dist(0, [-1]*N)
from_Snuke = dist(N-1, [-1]*N)
 
feneck = 0
for i,j in zip(from_feneck, from_Snuke):
    if i<=j:
        feneck += 1
    else:
        feneck -= 1
    
if feneck <= 0:
    print("Snuke")
else:
    print("Fennec")

