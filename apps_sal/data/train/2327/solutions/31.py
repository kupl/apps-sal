import sys


class BIT:

    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
        self.depth = n.bit_length()
        self.n0 = 1 << self.depth

    def get_sum(self, i):
        s = 0
        i += 1
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def query(self, l, r):
        return self.get_sum(r) - self.get_sum(l - 1)

    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def bisect_left(self, w):
        if w <= 0:
            return 0
        (x, k) = (0, self.n0)
        for _ in range(self.depth):
            k >>= 1
            if x + k <= self.size and self.tree[x + k] < w:
                w -= self.tree[x + k]
                x += k
        return x


read = sys.stdin.read
readline = sys.stdin.readline
(n, m, *lr) = map(int, read().split())
mp = iter(lr)
dlr = [(r - l + 1, l, r) for (l, r) in zip(mp, mp)]
dlr.sort(reverse=True)
ans = [0] * (m + 1)
b = BIT(m + 2)
for i in range(1, m + 1):
    while dlr and dlr[-1][0] < i:
        (d, l, r) = dlr.pop()
        b.add(l, 1)
        b.add(r + 1, -1)
    v = 0
    for j in range(i, m + 1, i):
        v += b.get_sum(j)
    ans[i] = len(dlr) + v
print(*ans[1:], sep='\n')
