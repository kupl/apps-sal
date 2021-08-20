from collections import deque
(n, m) = map(int, input().split())
plst = list(map(int, input().split()))
edges = [[] for _ in range(n)]
for _ in range(m):
    (x, y) = map(int, input().split())
    x -= 1
    y -= 1
    edges[x].append(y)
    edges[y].append(x)
check = [False for _ in range(n)]
uni = [0 for _ in range(n)]
pos = 0
queue = deque()
for i in range(n):
    if check[i]:
        continue
    pos += 1
    queue.append(i)
    check[i] = True
    while queue:
        now = queue.popleft()
        uni[now] += pos
        uni[plst[now] - 1] -= pos
        for aft in edges[now]:
            if check[aft]:
                continue
            check[aft] = True
            queue.append(aft)
print(uni.count(0))
