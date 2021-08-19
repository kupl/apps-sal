import sys


class Bit:
    def __init__(self, n):
        """
        :param n: number of elements
        """
        self.n = n
        self.tree = [0] * (n + 1)
        self.depth = n.bit_length() - 1

    def sum(self, i):
        """ return summation of elements in [0,i) """
        s = 0
        i -= 1
        while i >= 0:
            s += self.tree[i]
            i = (i & (i + 1)) - 1
        return s

    def build(self, array):
        """ bulid BIT from array """
        for i, a in enumerate(array):
            self.add(i, a)

    def add(self, i, x):
        """ add x to i-th element """
        while i < self.n:
            self.tree[i] += x
            i |= i + 1

    def get(self, i, j):
        """ return summation of elements in [i,j) """
        if i == 0:
            return self.sum(j)
        return self.sum(j) - self.sum(i)

    def lower_bound(self, x, equal=False):
        """
        return tuple = (return maximum i s.t. a0+a1+...+ai < x (if not existing, -1 ) , a0+a1+...+ai )
        if one wants to include equal (i.e., a0+a1+...+ai <= x), please set equal = True
        (Cation) We must assume that A_i>=0
        """
        sum_ = 0
        pos = -1    # 1-indexed の時は pos = 0
        if not equal:
            for i in range(self.depth, -1, -1):
                k = pos + (1 << i)
                if k < self.n and sum_ + self.tree[k] < x:  # 1-indexed の時は k <= self.n
                    sum_ += self.tree[k]
                    pos += 1 << i
        if equal:
            for i in range(self.depth, -1, -1):
                k = pos + (1 << i)
                if k < self.n and sum_ + self.tree[k] <= x:  # 1-indexed の時は k <= self.n
                    sum_ += self.tree[k]
                    pos += 1 << i
        return pos, sum_

    def __getitem__(self, i):
        """ [a0, a1, a2, ...] """
        return self.get(i, i + 1)

    def __iter__(self):
        """ [a0, a1, a2, ...] """
        for i in range(self.n):
            yield self.get(i, i + 1)

    def __str__(self):
        text1 = " ".join(["element:            "] + list(map(str, self)))
        text2 = " ".join(["cumsum(1-indexed):  "] + list(str(self.sum(i)) for i in range(1, self.n + 1)))
        return "\n".join((text1, text2))


class BitImos:
    def __init__(self, n):
        self.n = n
        self.p = Bit(self.n + 1)
        self.q = Bit(self.n + 1)

    def add(self, s, t, x):
        """ add x to a close-interval [s,t]"""
        t += 1
        self.p.add(s, -x * s)
        self.p.add(t, x * t)
        self.q.add(s, x)
        self.q.add(t, -x)

    def sum(self, s, t):
        """ return summation of elements in [s,t) """
        return self.p.sum(t) + self.q.sum(t) * t - self.p.sum(s) - self.q.sum(s) * s

    def __getitem__(self, s):
        """ return s-th element of array (not sum-array) """
        return self.q.sum(s + 1)

    def __iter__(self):
        """ max(self) returns what we obtain by the Imos method"""
        for t in range(self.n):
            yield self.q.sum(t + 1)

    def __str__(self):
        text1 = " ".join(["element: "] + list(map(str, self)))
        return text1


#############################################################
input = sys.stdin.readline

N, M = map(int, input().split())
data = [[] for _ in range(M + 1)]
for _ in range(N):
    l, r = map(int, input().split())
    data[r - l + 1].append((l, r))
B = BitImos(M + 1)
res = [0] * M
cnt = N
for d in range(1, M + 1):
    for l, r in data[d]:
        B.add(l, r, 1)
        cnt -= 1
    res[d - 1] += cnt
    for i in range(0, M + 1, d):
        res[d - 1] += B[i]
print(*res, sep="\n")
