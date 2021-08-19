import sys
from itertools import accumulate


class Lazysegtree:

    def __init__(self, A, intv, initialize=True, segf=min):
        self.N = len(A)
        self.N0 = 2 ** (self.N - 1).bit_length()
        self.intv = intv
        self.segf = segf
        self.lazy = [0] * (2 * self.N0)
        if initialize:
            self.data = [intv] * self.N0 + A + [intv] * (self.N0 - self.N)
            for i in range(self.N0 - 1, 0, -1):
                self.data[i] = self.segf(self.data[2 * i], self.data[2 * i + 1])
        else:
            self.data = [intv] * (2 * self.N0)

    def _ascend(self, k):
        k = k >> 1
        c = k.bit_length()
        for j in range(c):
            idx = k >> j
            self.data[idx] = self.segf(self.data[2 * idx], self.data[2 * idx + 1]) + self.lazy[idx]

    def _descend(self, k):
        k = k >> 1
        idx = 1
        c = k.bit_length()
        for j in range(1, c + 1):
            idx = k >> c - j
            ax = self.lazy[idx]
            if not ax:
                continue
            self.lazy[idx] = 0
            self.data[2 * idx] += ax
            self.data[2 * idx + 1] += ax
            self.lazy[2 * idx] += ax
            self.lazy[2 * idx + 1] += ax

    def query(self, l, r):
        L = l + self.N0
        R = r + self.N0
        Li = L // (L & -L)
        Ri = R // (R & -R)
        self._descend(Li)
        self._descend(Ri - 1)
        s = self.intv
        while L < R:
            if R & 1:
                R -= 1
                s = self.segf(s, self.data[R])
            if L & 1:
                s = self.segf(s, self.data[L])
                L += 1
            L >>= 1
            R >>= 1
        return s

    def add(self, l, r, x):
        L = l + self.N0
        R = r + self.N0
        Li = L // (L & -L)
        Ri = R // (R & -R)
        while L < R:
            if R & 1:
                R -= 1
                self.data[R] += x
                self.lazy[R] += x
            if L & 1:
                self.data[L] += x
                self.lazy[L] += x
                L += 1
            L >>= 1
            R >>= 1
        self._ascend(Li)
        self._ascend(Ri - 1)

    def binsearch(self, l, r, check, reverse=False):
        L = l + self.N0
        R = r + self.N0
        Li = L // (L & -L)
        Ri = R // (R & -R)
        self._descend(Li)
        self._descend(Ri - 1)
        (SL, SR) = ([], [])
        while L < R:
            if R & 1:
                R -= 1
                SR.append(R)
            if L & 1:
                SL.append(L)
                L += 1
            L >>= 1
            R >>= 1
        if reverse:
            for idx in SR + SL[::-1]:
                if check(self.data[idx]):
                    break
            else:
                return -1
            while idx < self.N0:
                ax = self.lazy[idx]
                self.lazy[idx] = 0
                self.data[2 * idx] += ax
                self.data[2 * idx + 1] += ax
                self.lazy[2 * idx] += ax
                self.lazy[2 * idx + 1] += ax
                idx = idx << 1
                if check(self.data[idx + 1]):
                    idx += 1
            return idx - self.N0
        else:
            for idx in SL + SR[::-1]:
                if check(self.data[idx]):
                    break
            else:
                return -1
            while idx < self.N0:
                ax = self.lazy[idx]
                self.lazy[idx] = 0
                self.data[2 * idx] += ax
                self.data[2 * idx + 1] += ax
                self.lazy[2 * idx] += ax
                self.lazy[2 * idx + 1] += ax
                idx = idx << 1
                if not check(self.data[idx]):
                    idx += 1
            return idx - self.N0

    def provfunc(self):
        idx = 1
        if self.data[1] >= 0:
            return -1
        while idx < self.N0:
            ax = self.lazy[idx]
            self.lazy[idx] = 0
            self.data[2 * idx] += ax
            self.data[2 * idx + 1] += ax
            self.lazy[2 * idx] += ax
            self.lazy[2 * idx + 1] += ax
            idx = idx << 1
            if self.data[idx + 1] < 0:
                idx += 1
        return idx - self.N0


(N, M) = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
table = [0] * (10 ** 6 + 1)
for a in A:
    table[a] -= 1
for b in B:
    table[b] += 1
table = list(accumulate(table[::-1]))[::-1]
T = Lazysegtree(table, 0, True, min)
Q = int(input())
Ans = [None] * Q
for q in range(Q):
    (t, i, x) = list(map(int, sys.stdin.readline().split()))
    i -= 1
    if t == 1:
        T.add(0, x + 1, -1)
        T.add(0, A[i] + 1, 1)
        A[i] = x
    else:
        T.add(0, x + 1, 1)
        T.add(0, B[i] + 1, -1)
        B[i] = x
    Ans[q] = T.provfunc()
print('\n'.join(map(str, Ans)))
