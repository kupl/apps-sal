from collections import deque


def bfs():
    q = deque()
    q.append(1)
    ans[1] = 1
    while q:
        i = q.popleft()
        for (j, c) in G[i]:
            if ans[j] == 0:
                if not ans[i] == c:
                    ans[j] = c
                else:
                    ans[j] = 1 if ans[i] >= 2 else 2
                q.append(j)
    return


(n, m) = map(int, input().split())
G = [[] for _ in range(n + 1)]
for _ in range(m):
    (u, v, c) = map(int, input().split())
    G[u].append([v, c])
    G[v].append([u, c])
ans = [0] * (n + 1)
bfs()
for i in range(1, n + 1):
    print(ans[i])
