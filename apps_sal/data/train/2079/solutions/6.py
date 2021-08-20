d = {}


def lca(x, y, w):
    res = 0
    while x != y:
        if x < y:
            (x, y) = (y, x)
        d[x] = d.get(x, 0) + w
        res += d[x]
        x //= 2
    return res


q = int(input())
while q > 0:
    q -= 1
    a = list(map(int, input().split()))
    if a[0] == 1:
        lca(a[1], a[2], a[3])
    else:
        print(lca(a[1], a[2], 0))
