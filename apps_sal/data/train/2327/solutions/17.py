from bisect import bisect
from operator import itemgetter

import sys
input = sys.stdin.readline

def inpl(): return list(map(int, input().split()))


class BIT:
    def __init__(self, N):
        self.size = 2 ** (int.bit_length(N)+1)
        self.tree = [0]*(self.size + 1)

    def sum(self, i):
        res = 0
        while i:
            res += self.tree[i]
            i -= (i & -(i))
        return res

    def add(self, i, x):
        if i == 0:
            return
        while i <= self.size:
            self.tree[i] += x
            i += (i & -(i))


class RABIT():
    # range add BIT
    def __init__(self, N):
        self.bit0 = BIT(N)
        self.bit1 = BIT(N)

    def sum(self, i):
        return i*self.bit1.sum(i) + self.bit0.sum(i)

    def add_range(self, l, r, x):
        self.bit0.add(l, -x*(l-1))
        self.bit1.add(l, x)
        self.bit0.add(r+1, x*r)
        self.bit1.add(r+1, -x)

    def get_range(self, l, r):
        return self.sum(r) - self.sum(l-1)


N, M = inpl()
R, L, S = [], [], []
Q = []
for _ in range(N):
    l, r = inpl()
    Q.append((l, r, (r-l+1)))

Q = sorted(Q, key=itemgetter(2), reverse=True)
rabit = RABIT(M+1)

Lmin = M
Rmax = 0
for i in range(1, M+1):
    while Q and Q[-1][2] < i:
        l, r, _ = Q.pop()
        rabit.add_range(l, r, 1)
        Lmin = min(Lmin, l)
        Rmax = max(Rmax, r)
    ans = len(Q)
    for j in range(-(-Lmin//i) * i, Rmax+1, i):
        ans += rabit.get_range(j, j)
    print(ans)

