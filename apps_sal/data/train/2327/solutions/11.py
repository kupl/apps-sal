class BIT(object):
    def __init__(self, size):
        self.size = size
        self.bit = [0] * (self.size + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.bit[i] += x
            i += i & -i

    def __str__(self):
        return str(self.bit)


n, m = list(map(int, input().split()))
lr = [[] for i in range(m + 1)]
for i in range(n):
    l, r = list(map(int, input().split()))
    lr[r - l + 1].append(l)

bit = BIT(m + 1)
t = 0
for d in range(1, m + 1):
    for l in lr[d]:
        bit.add(l, 1)
        bit.add(l + d, -1)

    t += len(lr[d])
    ans = n - t

    cur = 0
    while cur <= m:
        ans += bit.sum(cur)
        cur += d

    print(ans)
