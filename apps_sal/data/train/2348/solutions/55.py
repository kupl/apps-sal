import bisect


def dist(tree, tree_i, tree_j, parent, a, b):
    i = tree_i[b]
    if tree_i[a] == i:
        return tree_j[b] - tree_j[a]
    else:
        branch = tree[i]
        branch_root = branch[0]
        if branch_root < a:
            return tree_j[b] - bisect.bisect_left(branch, a) + 1
        else:
            p = parent[branch_root]
            if p < a:
                return tree_j[b] + 1
            else:
                return tree_j[b] + 1 + dist(tree, tree_i, tree_j, parent, a, p)


def solve(n, x, l, q, qry):
    g = [[] for _ in range(n)]
    parent = [-1] * n
    weight = [1] * n
    for v in range(1, n):
        p = bisect.bisect_left(x, x[v] - l)
        g[p].append(v)
        parent[v] = p
    for v in range(n - 1, -1, -1):
        for w in g[v]:
            weight[v] += weight[w]
    tree = [[0]]
    tree_i = [-1] * n
    tree_j = [0] * n
    tree_i[0] = 0
    for v in range(n):
        mw = 0
        c = -1
        for w in g[v]:
            if mw < weight[w]:
                mw = weight[w]
                c = w
        if 0 <= c:
            i = tree_i[v]
            tree[i].append(c)
            tree_i[c] = i
            tree_j[c] = len(tree[i]) - 1
            for w in g[v]:
                if w != c:
                    tree.append([w])
                    tree_i[w] = len(tree) - 1
    for tpl in qry:
        (a, b) = tpl
        if b < a:
            (a, b) = (b, a)
        print(dist(tree, tree_i, tree_j, parent, a, b))


def main():
    n = input()
    n = int(n)
    x = list(map(int, input().split()))
    l = input()
    l = int(l)
    q = input()
    q = int(q)
    qry = []
    for _ in range(q):
        (a, b) = input().split()
        a = int(a) - 1
        b = int(b) - 1
        qry.append((a, b))
    solve(n, x, l, q, qry)


def __starting_point():
    main()


__starting_point()
