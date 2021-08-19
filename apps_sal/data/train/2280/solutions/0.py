from bisect import bisect as br, bisect_left as bl
from collections import Counter
from itertools import accumulate
import sys
readline = sys.stdin.readline


class PMS:
    # 1-indexed
    def __init__(self, A, B, issum=False):
        # Aに初期状態の要素をすべて入れる,Bは値域のリスト
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
        # 座圧
        L2 = list(set(L))
        L2.sort()
        C = {v: k for k, v in enumerate(L2, 1)}
        # 1-indexed
        return L2, C

    def leng(self):
        # 今入っている個数を取得
        return self.count(self.X[-1])

    def count(self, v):
        # v(Bの元)以下の個数を取得
        i = self.comp[v]
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def less(self, v):
        # v(Bの元である必要はない)未満の個数を取得
        i = bl(self.X, v)
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def leq(self, v):
        # v(Bの元である必要はない)以下の個数を取得
        i = br(self.X, v)
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, v, x):
        # vをx個入れる,負のxで取り出す,iの個数以上取り出すとエラーを出さずにバグる
        i = self.comp[v]
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def get(self, i):
        # i番目の値を取得
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
        # 累積和がv以下となる最大のindexを返す
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
        # sumを扱いたいときにaddの代わりに使う
        self.add(i, x)
        x *= i
        i = self.comp[i]
        while i <= self.size:
            self.sumtree[i] += x
            i += i & -i

    def countsum(self, v):
        # v(Bの元)以下のsumを取得
        i = self.comp[v]
        s = 0
        while i > 0:
            s += self.sumtree[i]
            i -= i & -i
        return s

    def getsum(self, i):
        # i番目までのsumを取得
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
