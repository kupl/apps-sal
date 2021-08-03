from collections import deque
N, M = map(int, input().split())
P = list(map(int, input().split()))
P.insert(0, 0)
G = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    x, y = map(int, input().split())
    G[x].append(y)
    G[y].append(x)
col = [-1 for _ in range(N + 1)]
cnt = 0
for i in range(1, N + 1):
    if col[i] < 0:
        col[i] = cnt
        que = deque([i])
        while que:
            x = que.popleft()
            for y in G[x]:
                if col[y] < 0:
                    col[y] = cnt
                    que.append(y)
        cnt += 1
C = {c: [] for c in range(cnt)}
for i in range(1, N + 1):
    C[col[i]].append(i)
B = {c: [] for c in range(cnt)}
for c in C:
    for i in C[c]:
        B[c].append(P[i])
ans = 0
for c in C:
    a = set(C[c])
    b = set(B[c])
    ans += len(a & b)
print(ans)
