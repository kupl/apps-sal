from collections import defaultdict
import sys
input = sys.stdin.readline
'\n(駅、会社)を頂点にグラフを持つ。頂点数O(M)。\nそのまま辺を貼ると辺が多くなりすぎる。\n(駅、会社) -> (駅、無属性) -> (駅、会社)\n'
L = 32
mask = (1 << L) - 1
(N, M) = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    (p, q, c) = map(int, input().split())
    p <<= L
    q <<= L
    graph[p].append(p + c)
    graph[p + c].append(p)
    graph[q].append(q + c)
    graph[q + c].append(q)
    graph[p + c].append(q + c)
    graph[q + c].append(p + c)
INF = 10 ** 9
dist = defaultdict(lambda: INF)
start = 1 << L
goal = N << L
q = [start]
dist[start] = 0
d = 0
q0 = []
q1 = []
while q:
    for x in q:
        if x & mask == 0:
            for y in graph[x]:
                if dist[y] <= d + 1:
                    continue
                dist[y] = d + 1
                q1.append(y)
        else:
            for y in graph[x]:
                if dist[y] <= d:
                    continue
                dist[y] = d
                q0.append(y)
    if q0:
        q = q0
        q0 = []
        continue
    q = q1
    q1 = []
    d += 1
answer = dist[goal]
if answer == INF:
    answer = -1
print(answer)
