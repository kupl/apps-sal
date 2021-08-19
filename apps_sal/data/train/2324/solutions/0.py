import sys
sys.setrecursionlimit(10 ** 6)


def main():
    n = int(input())
    adj_list = [[] for i in range(n)]
    for i in range(n - 1):
        (a1, b1) = list(map(int, sys.stdin.readline().split()))
        adj_list[a1 - 1].append(b1 - 1)
        adj_list[b1 - 1].append(a1 - 1)
    path = list(reversed(dfs(0, -1, adj_list, n)))
    assert len(path) >= 2
    fpath = len(path) - len(path) // 2
    cut = set(path[fpath - 1:fpath + 1])
    f = dfs2(0, -1, adj_list, n, cut)
    s = dfs2(n - 1, -1, adj_list, n, cut)
    assert f + s == n
    print('Fennec' if f > s else 'Snuke')


def dfs(now, prev, adj_list, n):
    if now == n - 1:
        return [now]
    for next in adj_list[now]:
        if next == prev:
            continue
        p = dfs(next, now, adj_list, n)
        if p is not None:
            p.append(now)
            return p


def dfs2(now, prev, adj_list, n, cut):
    size = 1
    for next in adj_list[now]:
        if next == prev:
            continue
        if {now, next} == cut:
            continue
        s = dfs2(next, now, adj_list, n, cut)
        size += s
    return size


def __starting_point():
    main()


__starting_point()
