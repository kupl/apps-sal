from collections import defaultdict, deque
from heapq import heappush, heappop
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS(): return [list(x) for x in sys.stdin.readline().split()]


def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res


def IR(n):
    return [I() for i in range(n)]


def LIR(n):
    return [LI() for i in range(n)]


def SR(n):
    return [S() for i in range(n)]


def LSR(n):
    return [LS() for i in range(n)]


sys.setrecursionlimit(1000000)
mod = 1000000007


def A():
    n = I()
    a = LI()
    a.sort()
    f = [1] * n
    p = 0
    ans = 0
    while p < n:
        while p < n and not f[p]:
            p += 1
        if p == n:
            break
        ans += 1
        for i in range(n):
            if a[i] % a[p] == 0:
                f[i] = 0
    print(ans)
    return


def B():
    n = I()
    s = list(map(int, input()))
    g = LIR(n)
    ans = sum(s)
    for t in range(30000):
        for i in range(n):
            ai, bi = g[i]
            if t < bi:
                continue
            if (t - bi) % ai == 0:
                s[i] ^= 1
        su = sum(s)
        if ans < su:
            ans = su
    print(ans)
    return


def C():
    t = I()
    for _ in range(t):
        n = I()
        s = list(map(int, input()))
        mi = [s[-1]]
        for i in range(n - 1)[::-1]:
            mi.append(min(mi[-1], s[i]))
        mi = mi[::-1]
        ans = [None] * n
        for i in range(n):
            if mi[i] == s[i]:
                ans[i] = 1
            else:
                ans[i] = 2
        q = [s[i] for i in range(n) if ans[i] > 1]
        p = [q[i] for i in range(len(q))]
        p.sort()
        if p == q:
            for i in ans:
                print(i, end="")
            print()
        else:
            print("-")
    return


def D():
    def root(x):
        if x == par[x]:
            return x
        par[x] = root(par[x])
        return par[x]

    def unite(x, y):
        x = root(x)
        y = root(y)
        if rank[x] < rank[y]:
            par[x] = y
        else:
            par[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1

    n, k = LI()
    par = [i for i in range(n)]
    rank = [0] * n
    for i in range(k):
        x, y = LI()
        x -= 1
        y -= 1
        if root(x) != root(y):
            unite(x, y)
    size = [0] * n
    for i in range(n):
        size[root(i)] += 1
    ans = 0
    for i in size:
        if i > 0:
            ans += i - 1
    print(k - ans)
    return


def E():
    t = I()
    for _ in range(t):
        n, m = LI()
        s = LIR(n)
        s = [[s[i][j] for i in range(n)] for j in range(m)]
        if n <= m:
            ma = [max(s[i]) for i in range(m)]
            ma.sort(reverse=True)
            print(sum(ma[:n]))
        else:
            ans = 0
            k = [[]]
            for _ in range(m):
                k_ = []
                for i in range(n):
                    k_ += [x + [i] for x in k]
                k = [x for x in k_]
            for l in k:
                s_ = [[s[i][(j + l[i]) % n] for j in range(n)] for i in range(m)]
                print(l)
                p = sum([max([s_[i][j] for i in range(m)]) for j in range(n)])
                print(s_, p)
                if ans < p:
                    ans = p
            print(ans)
    return


def F():

    return


def G():
    def root(x):
        if x == par[x]:
            return x
        par[x] = root(par[x])
        return par[x]

    def unite(x, y):
        x = root(x)
        y = root(y)
        if rank[x] < rank[y]:
            par[x] = y
        else:
            par[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1

    m = 200000
    par = [i for i in range(m)]
    rank = [0] * m
    n, q = LI()
    a = LI()
    for i in range(n):
        a[i] -= 1
    count = defaultdict(lambda: 0)
    l = defaultdict(lambda: 0)
    lis = []
    for i in range(n):
        ai = a[i]
        if count[ai] == 0:
            l[ai] = i
            lis.append(ai)
        count[ai] += 1
    f = defaultdict(lambda: 0)
    r = defaultdict(lambda: 0)
    for i in range(n)[::-1]:
        ai = a[i]
        if not f[ai]:
            r[ai] = i
            f[ai] = 1
    f = [0] * n
    for i in lis:
        li, ri = l[i], r[i]
        f[li] += 1
        f[ri] -= 1
    for i in range(n - 1):
        if f[i] > 0:
            x, y = a[i], a[i + 1]
            if root(x) != root(y):
                unite(x, y)
        f[i + 1] += f[i]
    size = defaultdict(lambda: [])
    for i in l:
        size[root(i)].append(count[i])
    ans = 0
    for i in size.values():
        ans += sum(i) - max(i)
    print(ans)
    return


def H():

    return


def __starting_point():
    G()


__starting_point()
