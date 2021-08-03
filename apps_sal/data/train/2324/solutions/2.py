import sys
sys.setrecursionlimit(100000)

N = int(input())
G = [[] for i in range(N)]
for i in range(N - 1):
    a, b = (int(i) for i in input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

prev = [-1] * N


def DFS(start):
    res = 0
    for u in G[start]:
        if u != prev[start]:
            prev[u] = start
            res += DFS(u)
    return res + 1


DFS(0)
start = N - 1
path = [N - 1]
while True:
    path.append(prev[start])
    start = prev[start]
    if start == 0:
        break
path.reverse()
num = len(path)
c, d = (path[(num + 1) // 2 - 1], path[(num + 1) // 2])
G[c].remove(d)
G[d].remove(c)
prev = [-1] * N
DFS0 = DFS(0)
prev = [-1] * N
if DFS0 > DFS(N - 1):
    print("Fennec")
else:
    print("Snuke")
