from collections import defaultdict, deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
route = 10**6
Edges = defaultdict(set)
Visited = defaultdict(bool)
for _ in range(m):
    p, q, c = map(int, input().split())
    Edges[p].add(p + c * route)
    Edges[p + c * route].add(p)
    Edges[p + c * route].add(q + c * route)
    Edges[q + c * route].add(p + c * route)
    Edges[q].add(q + c * route)
    Edges[q + c * route].add(q)
q = deque()
q.append((1, 0))
cost = -1
while q:
    fr, c = q.popleft()
    Visited[fr] = True
    if fr == n:
        cost = c
        break
    for to in Edges[fr]:
        if Visited[to]:
            continue
        if fr <= 10**5 and to > route:
            q.append((to, c + 1))
        else:
            q.appendleft((to, c))
print(cost)
