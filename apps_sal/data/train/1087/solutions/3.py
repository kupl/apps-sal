import sys


def iter_dfs(G, s):
    (S, Q) = (set(), [])
    Q.append(s)
    p = Q.pop
    e = Q.extend
    t = S.add
    while Q:
        u = p()
        if u in S:
            continue
        t(u)
        e(G[u])
        yield u


def main():
    s = sys.stdin.readline
    (n, e) = list(map(int, s().split()))
    if e != n - 1:
        print('NO')
        return
    G = dict()
    for case in range(e):
        (n1, n2) = list(map(int, s().split()))
        if n1 not in G:
            G[n1] = [n2]
        else:
            G[n1].append(n2)
        if n2 not in G:
            G[n2] = [n1]
        else:
            G[n2].append(n1)
    tot = len(list(iter_dfs(G, 1)))
    if tot == n:
        print('YES')
    else:
        print('NO')


def __starting_point():
    main()


__starting_point()
