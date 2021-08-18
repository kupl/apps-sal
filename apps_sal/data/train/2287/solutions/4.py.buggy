import heapq
import sys
input = sys.stdin.readline
INF = 10 ** 18


n = int(input())
edges = [list(map(int, input().split())) for i in range(n - 1)]
k = int(input())
info = [list(map(int, input().split())) for i in range(k)]

tree = [[] for i in range(n)]
for a, b in edges:
    a -= 1
    b -= 1
    tree[a].append(b)
    tree[b].append(a)

ans = [INF] * n
q = []
for v, val in info:
    v -= 1
    ans[v] = val
    heapq.heappush(q, (-val, v))
    for nxt_v in tree[v]:
        if ans[nxt_v] != INF and abs(ans[v] - ans[nxt_v]) != 1:
            print("No")
            return

while q:
    val, v = heapq.heappop(q)
    val = -val
    for nxt_v in tree[v]:
        if ans[nxt_v] == INF:
            ans[nxt_v] = val - 1
            heapq.heappush(q, (-(val - 1), nxt_v))
        else:
            if abs(ans[v] - ans[nxt_v]) != 1:
                print("No")
                return

print("Yes")
for val in ans:
    print(val)
