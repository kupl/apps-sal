from bisect import bisect_left
import sys
input = sys.stdin.readline


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)


def main():
    N, Q = list(map(int, input().split()))
    kouji = [list(map(int, input().split())) for _ in range(N)]
    D = [int(input()) for _ in range(Q)]
    ans = [-1] * Q
    nxt = [i + 1 for i in range(Q)]
    uf = UnionFind(Q)
    kouji.sort(key=lambda x: x[2])
    for i in range(N):
        S, T, X = kouji[i]
        L = S - X
        R = T - X - 1
        L_idx = bisect_left(D, L)
        R_idx = bisect_left(D, R + 1)
        p = L_idx
        while p < R_idx:
            if ans[p] == -1:
                ans[p] = X
                uf.union(L_idx, p)
                nxt[p] = R_idx
                p += 1
            else:
                par = uf.find(p)
                p = nxt[par]
                uf.union(L_idx, par)
                par = uf.find(par)
                if nxt[par] < R_idx:
                    nxt[par] = R_idx
                if nxt[par] < p:
                    nxt[par] = p
    for i in range(Q):
        print((ans[i]))


def __starting_point():
    main()


__starting_point()
