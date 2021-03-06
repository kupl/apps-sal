import math
import sys
sys.setrecursionlimit(1000000)
N = int(input())
graph = {}
SCORE = 0


def dfs(visted, v, depth):
    visted[v] = depth
    for next_v in graph[v]:
        if visted[next_v] == -1:
            dfs(visted, next_v, depth + 1)


for _ in range(N - 1):
    (a, b) = list(map(int, input().split(' ')))
    if a not in graph:
        graph[a] = [b]
    else:
        graph[a].append(b)
    if b not in graph:
        graph[b] = [a]
    else:
        graph[b].append(a)
vF = [-1] * (N + 1)
vF[1] = 0
dfs(vF, 1, 0)
vS = [-1] * (N + 1)
vS[N] = 0
dfs(vS, N, 0)
fc = 0
sc = 0
for (f, s) in zip(vF[1:N + 1], vS[1:N + 1]):
    if f <= s:
        fc += 1
    else:
        sc += 1
if fc > sc:
    print('Fennec')
else:
    print('Snuke')
