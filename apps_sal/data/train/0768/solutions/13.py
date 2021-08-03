from sys import setrecursionlimit
setrecursionlimit(999999)


def children(g, n, child):
    if n in g.keys():
        x = 0
        for adg in g[n]:
            x += children(g, adg, child)
        child[n] = len(g[n]) + x
        return len(g[n]) + x
    else:
        child[n] = 0
        return 0


def check(g, n, child):
    if n in g.keys():
        x = 0
        for adg in g[n]:
            l = check(g, adg, child)
            if l > x:
                x = l
        if x > 0:
            return child[n] + 1 + x
    else:
        return 1


for _ in range(int(input())):
    n = int(input())
    a = [0] + list(map(int, input().split()))
    tree = {}
    for i in range(1, n):
        tree[a[i]] = tree.setdefault(a[i], [])
        tree[a[i]].append(i + 1)
    child = [0] * (n + 1)
    children(tree, 1, child)
    print(check(tree, 1, child))
