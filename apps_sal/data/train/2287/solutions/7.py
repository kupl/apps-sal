import sys
sys.setrecursionlimit(10**7)


def main0(n, ab, k, vp):
    ki = [[] for _ in range(n)]
    for a, b in ab:
        a, b = a - 1, b - 1
        ki[a].append(b)
        ki[b].append(a)
    lrf = [[-1, -1, -1, ] for _ in range(n)]
    for v, p in vp:
        v -= 1
        lrf[v] = [p, p, p % 2]
    flg = [True]

    def func(p, v):
        if lrf[v][2] != -1:
            l, r, f = lrf[v]
            # 親頂点との整合性
            if p >= 0:
                pl, pr, pf = lrf[p]
                if pl - 1 <= l <= pr + 1 and pf ^ f == 1:
                    # ok
                    pass
                else:
                    flg[0] = False
        else:
            # 親頂点から条件を計算
            pl, pr, pf = lrf[p]
            l, r, f = pl - 1, pr + 1, pf ^ 1
            lrf[v] = [l, r, f]
        l, r, f = lrf[v]
        for nv in ki[v]:
            if nv == p:
                continue
            # 子頂点たちの条件から、自分の条件を更新
            nl, nr, nf = func(v, nv)
            if f ^ nf == 0:
                flg[0] = False
            l = max(l, nl - 1)
            r = min(r, nr + 1)
            if l > r:
                flg[0] = False
        lrf[v] = [l, r, f]
        # 最終的な自分の条件を返す
        return (l, r, f)
    func(-1, vp[0][0] - 1)
    if not flg[0]:
        return []
    ret = [0] * n

    def func0(p, v):
        l, r, f = lrf[v]
        np = ret[p]
        if l <= np - 1 <= r and (np - 1) % 2 == f:
            ret[v] = np - 1
        elif l <= np + 1 <= r and (np + 1) % 2 == f:
            ret[v] = np + 1
        else:
            flg[0] = False
        for nv in ki[v]:
            if nv != p:
                func0(v, nv)
    ret[vp[0][0] - 1] = vp[0][1]
    for nv in ki[vp[0][0] - 1]:
        func0(vp[0][0] - 1, nv)
    if flg[0]:
        return ret
    else:
        return []


def __starting_point():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n - 1)]
    k = int(input())
    vp = [list(map(int, input().split())) for _ in range(k)]
    ret0 = main0(n, ab, k, vp)
    if len(ret0) == 0:
        print('No')
    else:
        print('Yes')
        for x in ret0:
            print(x)


__starting_point()
