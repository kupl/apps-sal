
cost = {}
tip = {}


d = {
    1: [(2, 1, 0), (3, 1, 0), (4, 0, 0), (3, 0, 1), (2, 0, 0), (4, 0, 1), (3, 1, 1)],
    2: [(1, 0, 0), (3, 0, 1), (4, 0, 1), (1, -1, 0), (3, 0, 0), (4, -1, 0), (4, -1, 1)],
    3: [(2, 0, 0), (1, -1, 0), (4, -1, 0), (4, 0, 0), (1, 0, -1), (2, 0, -1), (1, -1, -1)],
    4: [(1, 0, -1), (2, 0, -1), (3, 0, 0), (1, 0, 0), (2, 1, 0), (3, 1, 0), (2, 1, -1)]
}


def dfs(t, x, y, dist, cost):
    if dist >= 4:
        return []

    if (t, x, y) in cost:
        cost[(t, x, y)] = min(cost[(t, x, y)], dist)
    else:
        cost[(t, x, y)] = dist

    for e in d[t]:
        dfs(e[0], x + e[1], y + e[2], dist + 1, cost)


tip[((0, 1), (1, 0))] = 1
tip[((1, 0), (0, 1))] = 1

tip[((0, -1), (1, 0))] = 4
tip[((1, 0), (0, -1))] = 4

tip[((0, 1), (-1, 0))] = 2
tip[((-1, 0), (0, 1))] = 2

tip[((0, -1), (-1, 0))] = 3
tip[((-1, 0), (0, -1))] = 3


def test(a, b, c):
    if b[0] != c[0] and b[1] != c[1]:
        return True
    return False


def dd(a, b):
    return (b[0] - a[0], b[1] - a[1])


def conv(coords):

    a = (coords[0], coords[1])
    b = (coords[2], coords[3])
    c = (coords[4], coords[5])

    center = a
    o1 = b
    o2 = c

    if test(b, a, c):
        center = b
        o1 = a
        o2 = c

    if test(c, a, b):
        center = c
        o1 = a
        o2 = b

    tp = tip[(dd(center, o1), dd(center, o2))]
    (x, y) = center
    return (tp, x, y)


def sgn(tp, dx, dy):
    if tp == 1 or tp == 3:
        if dx * dy <= 0:
            return 0
        return 1

    if dx * dy <= 0:
        return 1
    return 0


def get_cost(tp, x, y, xf, yf):
    diag = min(abs(x - xf), abs(y - yf))
    lin = max(abs(x - xf), abs(y - yf))

    return 2 * lin + sgn(tp, x - xf, y - yf) * 10


def solve(coords):

    (t, x, y) = conv(coords)

    to = {}

    dfs(t, x, y, 0, to)

    ans = 1e18

    for e in cost:
        for f in to:
            if f[0] == e[0]:
                ans = min(ans, cost[e] + to[f] + get_cost(e[0], e[1], e[2], f[1], f[2]))

    return ans


lst = dfs(1, 0, 0, 0, cost)


n = int(input())
for i in range(n):
    coords = list(map(int, input().split()))
    print((solve(coords)))
