import sys
input = sys.stdin.readline

n, m = map(int, input().split())
C = [list(map(int, input().split())) for i in range(n)]


class Bit:  # Fenwick Tree と同じ
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, l, r):  # [l,r)の和を求める
        # 内部的には[l+1,r+1)の和つまり(rまでの和-lまでの和)
        s = 0
        while r > 0:
            s += self.tree[r]
            r -= r & -r  # 2進数の最も下位の1を取り除くという意味(例:1010→1000)
        while l > 0:
            s -= self.tree[l]
            l -= l & -l  # 2進数の最も下位の1を取り除くという意味(例:1010→1000)
        return s

    def add(self, i, x):  # i番目にxを足す
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i  # 2進数の最も下位の1を繰り上げるという意味(例:1010→1100)

    def sett(self, i, x):  # i番目をxにする
        self.add(i, x - self.sum(i, i + 1))

    def print_bit(self):  # 内部状態をindex順に出力
        print([self.sum(i, i + 1) for i in range(self.size)])

    def print_sum(self):  # 累積和をindex順に出力
        print([self.sum(0, i + 1) for i in range(self.size)])

    def lower_bound_left(self, w):  # xまでの和がw以上となる最小のx、総和がw未満の場合nが返る
        n = self.size
        r = 1
        x = 0
        if self.sum(0, n) < w:
            return n
        while r < n:
            r *= 2
        le = r
        while le > 0:
            if (x + le < n and self.tree[x + le] < w):
                w -= self.tree[x + le]
                x += le
            le //= 2
        return x

    def upper_bound_left(self, w):  # xまでの和がwより大きくなる最小のx、総和がw以下の場合nが返る
        n = self.size
        r = 1
        x = 0
        if self.sum(0, n) <= w:
            return n
        while r < n:
            r *= 2
        le = r
        while le > 0:
            if (x + le < n and self.tree[x + le] <= w):
                w -= self.tree[x + le]
                x += le
            le //= 2
        return x

    def lower_bound_right(self, w):  # xまでの和がw以下となる最大のx、0番目がwより大きい場合-1が返る
        return self.upper_bound_left(w) - 1

    def upper_bound_right(self, w):  # xまでの和がw未満となる最大のx、0番目がw以上の場合-1が返る
        return self.lower_bound_left(w) - 1


D = [[] for i in range(m + 1)]
for d in range(1, m + 1):
    for j in range(d, m + 1, d):
        D[j].append(d)

L = [0] * (m + 1)
for i in range(1, m + 1):
    for j in range(len(D[i])):
        L[D[i][j]] = i

# print(D)

A = [-1] * (m + 1)
B = Bit(m + 2)
E = [0] * (m + 1)
ANS = [0] * (m + 1)

C.sort(key=lambda x: x[1])
# print(C)
ind = 0
# mul = 1
for i in range(1, m + 1):
    # print(i)
    for j in range(len(D[i])):
        k = D[i][j]
        if A[k] != -1:
            ANS[k] += B.sum(0, A[k] + 1)
        E[i] += 1
        A[k] = i
        # print(E)
    while ind < n and C[ind][1] <= i:
        l = C[ind][0]
        r = C[ind][1]
        B.add(l, 1)
        B.add(r + 1, -1)
        # mul -= 1
        ind += 1

for i in range(1, m + 1):
    ANS[i] += B.sum(0, L[i] + 1)

for i in range(1, m + 1):
    print(ANS[i])
