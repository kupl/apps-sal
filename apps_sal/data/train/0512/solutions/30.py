import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)


def read_values():
    return list(map(int, input().split()))


def read_index():
    return [int(x) - 1 for x in input().split()]


def read_list():
    return list(read_values())


def read_lists(N):
    return [read_list() for n in range(N)]


class V:
    def __init__(self, f, v=None):
        self.f = f
        self.v = v

    def __str__(self):
        return str(self.v)

    def ud(self, n):
        if n is None:
            return

        if self.v is None:
            self.v = n
            return
        self.v = self.f(self.v, n)


class LCA:
    def __init__(self, N, L):
        self.L = L
        self.INF = (N, None)
        self.M0 = 2 ** (2 * N - 1).bit_length()
        self.data = [self.INF] * (2 * self.M0)
        self.D = [0] * N
        self.F = [0] * N
        self.S = []
        self.dist = [0] * N

        self.dfs1(0, 0, -1)
        for i, v in enumerate(self.S):
            self.data[self.M0 - 1 + i] = (self.D[v], i)
        for i in range(self.M0 - 2, -1, -1):
            self.data[i] = min(self.data[2 * i + 1], self.data[2 * i + 2])

    def dfs1(self, v, d, p, pd=0):
        self.F[v] = len(self.S)
        self.D[v] = d
        self.S.append(v)
        self.dist[v] = pd
        for w, c, dis in self.L[v]:
            if w == p:
                continue
            self.dfs1(w, d + 1, v, pd + dis)
            self.S.append(v)

    def _query(self, a, b):
        yield self.INF
        a += self.M0
        b += self.M0
        while a < b:
            if b & 1:
                b -= 1
                yield self.data[b - 1]
            if a & 1:
                yield self.data[a - 1]
                a += 1
            a >>= 1
            b >>= 1

    def query(self, u, v):
        fu = self.F[u]
        fv = self.F[v]
        if fu > fv:
            fu, fv = fv, fu
        return self.S[min(self._query(fu, fv + 1))[1]]

    def dist(self, v):
        return self.dist[v]


def dfs2(L, v, p, QS, ans, CC, CD):
    for q, x, y, f in QS[v]:
        ans[q] += (y * CC[x] - CD[x]) * f

    for w, c, dis in L[v]:
        if w == p:
            continue
        CC[c] += 1
        CD[c] += dis
        dfs2(L, w, v, QS, ans, CC, CD)
        CC[c] -= 1
        CD[c] -= dis


def main():
    N, Q = read_values()
    L = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b, c, d = read_values()
        a -= 1
        b -= 1
        c -= 1
        L[a].append((b, c, d))
        L[b].append((a, c, d))

    g = LCA(N, L)

    QS = [[] for _ in range(N)]
    ans = [0] * Q
    for q in range(Q):
        x, y, u, v = read_values()
        x -= 1
        u -= 1
        v -= 1
        w = g.query(u, v)
        ans[q] = g.dist[u] + g.dist[v] - 2 * g.dist[w]
        QS[u].append((q, x, y, 1))
        QS[v].append((q, x, y, 1))
        QS[w].append((q, x, y, -2))

    CC = [0] * N
    CD = [0] * N
    dfs2(L, 0, -1, QS, ans, CC, CD)

    print(("\n".join(map(str, ans))))


def __starting_point():
    main()


__starting_point()
