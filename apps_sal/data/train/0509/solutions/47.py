from collections import defaultdict, deque
n, m = map(int, input().split())
G = defaultdict(list)
for _ in range(m):
    i, j, w = map(int, input().split())
    G[i].append((j, w))
    G[j].append((i, w))
ans = [0] * (n + 1)
ans[1] = 1
q = deque([1])
while q:
    node = q.popleft()
    for nei, w in G[node]:
        if ans[nei]:
            continue
        if ans[node] == w:
            ans[nei] = w + 1 if w < n else 1
        else:
            ans[nei] = w
        q.append(nei)

for i in range(n):
    print(ans[i + 1])
