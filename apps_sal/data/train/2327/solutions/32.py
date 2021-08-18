import sys
input = sys.stdin.readline


class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
        self.base = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        self.base[i] += x
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def get(self, i):
        return self.base[i]


class RangeUpdate:
    def __init__(self, n):
        self.p = Bit(n + 1)
        self.q = Bit(n + 1)

    def add(self, s, t, x):
        t += 1
        self.p.add(s, -x * s)
        self.p.add(t, x * t)
        self.q.add(s, x)
        self.q.add(t, -x)

    def sum(self, s, t):
        t += 1
        return self.p.sum(t) + self.q.sum(t) * t - \
            self.p.sum(s) - self.q.sum(s) * s

    def get(self, s):
        return self.p.get(s + 1) + self.q.get(s + 1) * (s + 1) + self.q.sum(s)


n, m = [int(i) for i in input().split()]
lr = [[int(i) for i in input().split()] for _ in range(n)]

lr.sort(key=lambda x: x[1] - x[0])


omiyage = RangeUpdate(m + 1)
index = 0
for d in range(1, m + 1):
    while(index < n and lr[index][1] - lr[index][0] < d):
        omiyage.add(lr[index][0] + 1, lr[index][1] + 1, 1)
        index += 1
    ans = 0
    pos = 0
    while(pos <= m):
        ans += omiyage.get(pos + 1)
        pos += d
    ans += n - index
    print(ans)
