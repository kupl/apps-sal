from itertools import combinations_with_replacement 
from collections import deque

#sys.stdin = open("input_py.txt","r")

n, m = map(int, input().split())
G = [ [] for i in range(n)]

for i in range(m):
    x, y = map(int, input().split())
    x-=1; y-=1
    G[x].append(y)
    G[y].append(x)

def BFS(s):
    dist = [-1 for i in range(n)]
    dist[s] = 0
    Q = deque()
    Q.append(s)
    while len(Q) > 0:
        v = Q.popleft()
        for to in G[v]:
            if dist[to] < 0:
                dist[to] = dist[v] + 1
                Q.append(to)
    return dist 


Dist = [BFS(i) for i in range(n)]

s1, t1, l1 = map(int, input(). split())
s2, t2, l2 = map(int, input(). split())
s1-=1; t1-=1; s2-=1; t2-=1
if Dist[s1][t1] > l1 or Dist[s2][t2] > l2:
    print(-1)
    return

rest = Dist[s1][t1] + Dist[s2][t2]

for i in range(n):
    for j in range(n):
        if Dist[i][s1] + Dist[i][j] + Dist[j][t1] <= l1 and Dist[i][s2] + Dist[i][j] + Dist[j][t2] <= l2 :
            rest = min(rest, Dist[i][j] + Dist[i][s1] + Dist[i][s2] + Dist[j][t1] + Dist[j][t2])
        if Dist[i][s1] + Dist[i][j] + Dist[j][t1] <= l1 and Dist[j][s2] + Dist[i][j] + Dist[i][t2] <= l2 :
            rest = min(rest, Dist[i][j] + Dist[j][t1] + Dist[j][s2] + Dist[i][s1] + Dist[i][t2])
print(m-rest)
