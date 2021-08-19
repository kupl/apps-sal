class FTree:

    def __init__(self, f):

        self.n = len(f)

        self.ft = [0] * (self.n + 1)

        for i in range(1, self.n + 1):

            self.ft[i] += f[i - 1]

            if i + self.lsone(i) <= self.n:

                self.ft[i + self.lsone(i)] += self.ft[i]

    def lsone(self, s):

        return s & (-s)

    def query(self, i, j):

        if i > 1:

            return self.query(1, j) - self.query(1, i - 1)

        s = 0

        while j > 0:

            s += self.ft[j]

            j -= self.lsone(j)

        return s

    def update(self, i, v):

        while i <= self.n:

            self.ft[i] += v

            i += self.lsone(i)

    def select(self, k):

        lo = 1

        hi = self.n

        for i in range(19):  # 30

            mid = (lo + hi) // 2

            if self.query(1, mid) < k:

                lo = mid

            else:

                hi = mid

        return hi


n = int(input())
data = [int(i) for i in input().split()]
ft = FTree(list(range(1, n + 1)))
ans = [""] * n

for i in range(n - 1, -1, -1):
    val = data[i]
    ind = ft.select(val + 1)
    ans[i] = str(ind)
    ft.update(ind, -ind)

print(" ".join(ans))
