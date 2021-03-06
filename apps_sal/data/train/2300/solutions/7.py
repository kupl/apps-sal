import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def int1(x):
    return int(x) - 1


def p2D(x):
    return print(*x, sep='\n')


def main():

    def dfs(u=0):

        def merge(dpu, dpv):
            vn = len(dpv)
            for d in range(-1, -1 - vn, -1):
                (u0, u1, u2) = dpu[d]
                (v0, v1, v2) = dpv[d]
                n0 = u0 * v0 % md
                n1 = (u0 * v1 + u1 * v0) % md
                n2 = (u2 * (v0 + v1 + v2) + v2 * (u0 + u1) + u1 * v1) % md
                dpu[d] = (n0, n1, n2)
        if len(to[u]) == 0:
            return [(inv2, inv2, 0)]
        dpu = []
        mxlen = 0
        for v in to[u]:
            dpv = dfs(v)
            if not dpu:
                dpu = dpv
            else:
                if len(dpu) < len(dpv):
                    (dpu, dpv) = (dpv, dpu)
                mxlen = max(mxlen, len(dpv))
                merge(dpu, dpv)
        for d in range(-1, -1 - mxlen, -1):
            (u0, u1, u2) = dpu[d]
            dpu[d] = (u0 + u2, u1, 0)
        dpu.append((inv2, inv2, 0))
        return dpu
    md = 10 ** 9 + 7
    inv2 = pow(2, md - 2, md)
    n = int(input())
    to = [[] for _ in range(n + 1)]
    pp = list(map(int, input().split()))
    for (i, p) in enumerate(pp, 1):
        to[p].append(i)
    dp0 = dfs()
    ans = sum((u1 for (_, u1, _) in dp0))
    print(ans * pow(2, n + 1, md) % md)


main()
