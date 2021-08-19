def dfs(s):
    if v[s] == 1:
        return
    v[s] = 1
    for k in adj[s]:
        dfs(k)


test = int(input())
for t in range(test):
    (n, m) = map(int, input().split())
    v = [0 for i in range(n)]
    adj = [[] for i in range(n)]
    for i in range(m):
        (a, b) = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    count = 0
    while 0 in v:
        node = v.index(0)
        dfs(node)
        count += 1
    print(count)
