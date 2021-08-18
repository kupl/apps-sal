import collections


def lca(u, v):
    ub = bin(u)[2:]
    vb = bin(v)[2:]

    r = 0
    for i, (a, b) in enumerate(zip(ub, vb)):
        if a != b:
            break
        r = r * 2 + int(a)
    return r


def add(cost, n, root, w):
    while n > root:
        cost[n] += w
        n //= 2


def get(cost, n, root):
    r = 0
    while n > root:
        r += cost[n]
        n //= 2
    return r


def __starting_point():
    q = int(input())

    cost = collections.Counter()
    for _ in range(q):
        cmd = list(map(int, input().split()))
        if cmd[0] == 1:
            v, u, w = cmd[1:]
            root = lca(v, u)
            add(cost, v, root, w)
            add(cost, u, root, w)
        else:
            v, u = cmd[1:]
            root = lca(v, u)
            print(get(cost, v, root) + get(cost, u, root))


__starting_point()
