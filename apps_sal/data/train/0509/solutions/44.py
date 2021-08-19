import sys
input = sys.stdin.readline
(n, m) = map(int, input().split())
G = [[] for _ in range(n + 1)]
for _ in range(m):
    (u, v, c) = map(int, input().split())
    G[u].append((v, c))
    G[v].append((u, c))
q = 1
stack = [1]
ans = [0] * (n + 1)
ans[1] = 1
while stack:
    v = stack.pop()
    for (u, c) in G[v]:
        if not ans[u]:
            if ans[v] == c:
                c = c % n + 1
            ans[u] = c
            stack.append(u)
            q += 1
            if q == n:
                stack = []
                break
if q == n:
    print(*ans[1:], sep='\n')
else:
    print('No')
