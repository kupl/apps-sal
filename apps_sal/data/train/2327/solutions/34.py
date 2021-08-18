import sys
input = sys.stdin.readline

n, m = map(int, input().split())
C = [list(map(int, input().split())) for i in range(n)]


class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, l, r):
        s = 0
        while r > 0:
            s += self.tree[r]
            r -= r & -r
        while l > 0:
            s -= self.tree[l]
            l -= l & -l
        return s

    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def sett(self, i, x):
        self.add(i, x - self.sum(i, i + 1))

    def print_bit(self):
        print([self.sum(i, i + 1) for i in range(self.size)])

    def print_sum(self):
        print([self.sum(0, i + 1) for i in range(self.size)])

    def lower_bound_left(self, w):
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

    def upper_bound_left(self, w):
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

    def lower_bound_right(self, w):
        return self.upper_bound_left(w) - 1

    def upper_bound_right(self, w):
        return self.lower_bound_left(w) - 1


D = [[] for i in range(m + 1)]
for d in range(1, m + 1):
    for j in range(d, m + 1, d):
        D[j].append(d)

L = [0] * (m + 1)
for i in range(1, m + 1):
    for j in range(len(D[i])):
        L[D[i][j]] = i


A = [-1] * (m + 1)
B = Bit(m + 2)
E = [0] * (m + 1)
ANS = [0] * (m + 1)

C.sort(key=lambda x: x[1])
ind = 0
for i in range(1, m + 1):
    for j in range(len(D[i])):
        k = D[i][j]
        if A[k] != -1:
            ANS[k] += B.sum(0, A[k] + 1)
        E[i] += 1
        A[k] = i
    while ind < n and C[ind][1] <= i:
        l = C[ind][0]
        r = C[ind][1]
        B.add(l, 1)
        B.add(r + 1, -1)
        ind += 1

for i in range(1, m + 1):
    ANS[i] += B.sum(0, L[i] + 1)

for i in range(1, m + 1):
    print(ANS[i])
