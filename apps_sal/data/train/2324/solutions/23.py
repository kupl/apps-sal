n = int(input())
node = [[] for _ in range(n)]
for _ in range(n - 1):
    (a, b) = map(int, input().split())
    node[a - 1].append(b - 1)
    node[b - 1].append(a - 1)
visited = [False] * n


def dfs(i):
    dis = [-1] * n
    dis[i] = 0
    stack = [i]
    while stack:
        p = stack.pop()
        for x in node[p]:
            if dis[x] == -1:
                dis[x] = dis[p] + 1
                stack.append(x)
    return dis


(d0, dn) = (dfs(0), dfs(n - 1))
cnt = 0
for i in range(n):
    if d0[i] > dn[i]:
        cnt += 1
if cnt >= n / 2:
    print('Snuke')
else:
    print('Fennec')
