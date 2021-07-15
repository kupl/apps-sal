N = int(1e5+3)
n = int(input())
adj = list([] for i in range(N))
for _ in range(n-1):
    u, v = list(map(int, input().split()))
    adj[u].append(v)
    adj[v].append(u)
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))

def dfs(u, p, c_lvl, p_lvl, d):
    stk = [(u, p, c_lvl, p_lvl)]
    while stk:
        (u, p, c_lvl, p_lvl) = stk.pop()
        if c_lvl != d[u]:
            c_lvl = 1 - c_lvl
            res.append(str(u))
        for v in adj[u]:
            if v != p:
                stk += [(v, u, p_lvl, c_lvl)]

d = [i ^ j for (i, j) in zip(a, b)]
res = []
dfs(1, 0, 0, 0, d)
print(len(res))
print('\n'.join(res))

