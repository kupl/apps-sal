I = input
n = int(I())
d = {}


def lca(u, v, w):
    res = 0
    while u != v:
        if u < v:
            u, v = v, u
        d[u] = d.get(u, 0) + w
        res += d[u]
        u = u // 2
    return res


for i in range(n):
    l = list(map(int, I().split()))
    if l[0] == 1:
        lca(l[1], l[2], l[3])
    else:
        print(lca(l[1], l[2], 0))
