n = int(input())
edges = [[] for _ in range(n)]
for _ in range(n - 1):
    (a, b) = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)
dp = [0] * n
dp[0] = 1
fp = [0] * n
fp[n - 1] = 1


def bfs(u):
    q = []
    q.append(u)
    while q:
        p = q.pop()
        for i in edges[p]:
            if dp[i] == 0:
                q.append(i)
                dp[i] += dp[p] + 1


def ffs(u):
    q = []
    q.append(u)
    while q:
        p = q.pop()
        for i in edges[p]:
            if fp[i] == 0:
                q.append(i)
                fp[i] += fp[p] + 1


bfs(0)
ffs(n - 1)
c = 0
for i in range(n):
    if dp[i] <= fp[i]:
        c += 1
if 2 * c > n:
    print('Fennec')
else:
    print('Snuke')
