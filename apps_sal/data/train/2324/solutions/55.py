def dfs(x):
    d = [-1] * (N + 1)
    stack = [x]
    while stack:
        x = stack.pop()
        for i in G[x]:
            if d[i] == -1:
                d[i] = d[x] + 1
                stack.append(i)
    return d

N = int(input())
G = [set() for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a].add(b)
    G[b].add(a)

d1, dn = dfs(1), dfs(N)
num = 0
for i in range(1, N + 1):
    if d1[i] <= dn[i]:
        num += 1
if num > N // 2:
    print('Fennec')
else:
    print('Snuke')
