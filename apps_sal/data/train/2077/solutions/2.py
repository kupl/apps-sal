class DisjointSet:
    def __init__(self, n):
        self._fa = list(range(n))

    def union(self, x, y):
        x = self.get_father(x)
        y = self.get_father(y)
        self._fa[x] = y
        return y

    def get_father(self, x):
        y = self._fa[x]
        if self._fa[y] == y:
            return y
        else:
            z = self._fa[y] = self.get_father(y)
            return z

    def __repr__(self):
        return repr([self.get_father(i) for i in range(len(self._fa))])


def solve(n, a, b, xs):
    h = {x: i for i, x in enumerate(xs)}
    if a == b:
        if all(a - x in h for x in xs):
            return [0] * n
        return False
    g1 = n
    g2 = n + 1
    ds = DisjointSet(n + 2)

    for i, x in enumerate(xs):
        for t in (a, b):
            if t - x in h:
                ds.union(i, h[t - x])

    for i, x in enumerate(xs):
        b1 = (a - x) in h
        b2 = (b - x) in h
        if b1 + b2 == 0:
            return False
        if b1 + b2 == 1:
            if b1:
                ds.union(i, g1)
            else:
                ds.union(i, g2)
            if ds.get_father(g1) == ds.get_father(g2):
                return False
    group = [None] * n
    for i, x in enumerate(xs):
        f = ds.get_father(i)
        if f < n:
            return False
        group[i] = f - n
    return group


n, a, b = map(int, input().split())
xs = list(map(int, input().split()))
group = solve(n, a, b, xs)
if isinstance(group, list):
    print('YES')
    print(' '.join(map(str, group)))
else:
    print('NO')
