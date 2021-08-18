from bisect import bisect as br, bisect_left as bl
from collections import Counter
from itertools import accumulate
import sys
readline = sys.stdin.readline


class PMS:
    def __init__(self, A, B, issum=False):
        self.X, self.comp = self.compress(B)
        self.size = len(self.X)
        self.tree = [0] * (self.size + 1)
        self.p = 2**(self.size.bit_length() - 1)
        self.dep = self.size.bit_length()

        CA = Counter(A)
        S = [0] + list(accumulate([CA[self.X[i]] for i in range(self.size)]))
        for i in range(1, 1 + self.size):
            self.tree[i] = S[i] - S[i - (i & -i)]
        if issum:
            self.sumtree = [0] * (self.size + 1)
            Ssum = [0] + list(accumulate([CA[self.X[i]] * self.X[i] for i in range(self.size)]))
            for i in range(1, 1 + self.size):
                self.sumtree[i] = Ssum[i] - Ssum[i - (i & -i)]

    def compress(self, L):
        L2 = list(set(L))
        L2.sort()
        C = {v: k for k, v in enumerate(L2, 1)}
        return L2, C

    def leng(self):
        return self.count(self.X[-1])

    def count(self, v):
        i = self.comp[v]
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def less(self, v):
        i = bl(self.X, v)
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def leq(self, v):
        i = br(self.X, v)
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, v, x):
        i = self.comp[v]
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def get(self, i):
        if i <= 0:
            return -1
        s = 0
        k = self.p
        for _ in range(self.dep):
            if s + k <= self.size and self.tree[s + k] < i:
                s += k
                i -= self.tree[s]
            k //= 2
        return self.X[s]

    def gets(self, v):
        v1 = v
        s = 0
        k = self.p
        for _ in range(self.dep):
            if s + k <= self.size and self.sumtree[s + k] < v:
                s += k
                v -= self.sumtree[s]
            k //= 2
        if s == self.size:
            return self.leng()
        return self.count(self.X[s]) + (v1 - self.countsum(self.X[s])) // self.X[s]

    def addsum(self, i, x):
        self.add(i, x)
        x *= i
        i = self.comp[i]
        while i <= self.size:
            self.sumtree[i] += x
            i += i & -i

    def countsum(self, v):
        i = self.comp[v]
        s = 0
        while i > 0:
            s += self.sumtree[i]
            i -= i & -i
        return s

    def getsum(self, i):
        x = self.get(i)
        return self.countsum(x) - x * (self.count(x) - i)


N, Q = map(int, readline().split())
P = list(map(int, readline().split()))
MOD = 998244353
T = [100 * pow(pi, MOD - 2, MOD) % MOD for pi in P]

AT = [None] * N
AT[0] = T[0]
for i in range(1, N):
    AT[i] = (AT[i - 1] + 1) * T[i] % MOD
AM = [None] * N
AMi = [None] * N
AM[0] = T[0]
for i in range(1, N):
    AM[i] = AM[i - 1] * T[i] % MOD
AMi[N - 1] = pow(AM[N - 1], MOD - 2, MOD)
for i in range(N - 2, -1, -1):
    AMi[i] = AMi[i + 1] * T[i + 1] % MOD
AT += [0]
AM += [1]
AMi += [1]

Ans = [None] * Q
kk = set([0, N])
PM = PMS([0, N], list(range(N + 1)))
ans = AT[N - 1]
for qu in range(Q):
    f = int(readline()) - 1
    if f not in kk:
        kk.add(f)
        PM.add(f, 1)
        fidx = PM.count(f)
        fm = PM.get(fidx - 1)
        fp = PM.get(fidx + 1)
        am = (AT[f - 1] - AM[f - 1] * AMi[fm - 1] * AT[fm - 1]) % MOD
        ap = (AT[fp - 1] - AM[fp - 1] * AMi[f - 1] * AT[f - 1]) % MOD
        aa = (AT[fp - 1] - AM[fp - 1] * AMi[fm - 1] * AT[fm - 1]) % MOD
        ans = (ans - aa + am + ap) % MOD
    else:
        kk.remove(f)
        fidx = PM.count(f)
        fm = PM.get(fidx - 1)
        fp = PM.get(fidx + 1)
        PM.add(f, -1)
        am = (AT[f - 1] - AM[f - 1] * AMi[fm - 1] * AT[fm - 1]) % MOD
        ap = (AT[fp - 1] - AM[fp - 1] * AMi[f - 1] * AT[f - 1]) % MOD
        aa = (AT[fp - 1] - AM[fp - 1] * AMi[fm - 1] * AT[fm - 1]) % MOD
        ans = (ans + aa - am - ap) % MOD
    Ans[qu] = ans
print('\n'.join(map(str, Ans)))
