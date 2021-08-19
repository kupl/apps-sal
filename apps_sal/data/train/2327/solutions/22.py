import sys
input = sys.stdin.readline
(N, M) = map(int, input().split())
a = []
for i in range(N):
    (l, r) = map(int, input().split())
    a.append((l, r))
a.sort(key=lambda x: x[0] - x[1])


class BIT:

    def __init__(self, n):
        self.n = n
        self.data = [0] * (n + 1)
        self.el = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def add(self, i, x):
        self.el[i] += x
        while i <= self.n:
            self.data[i] += x
            i += i & -i

    def get(self, i, j=None):
        if j is None:
            return self.el[i]
        return self.sum(j) - self.sum(i)

    def lowerbound(self, s):
        x = 0
        y = 0
        for i in range(self.n.bit_length(), -1, -1):
            k = x + (1 << i)
            if k <= self.n and y + self.data[k] < s:
                y += self.data[k]
                x += 1 << i
        return x + 1


fwk = BIT(M + 1)
for l in range(1, M + 1):
    res = len(a)
    for x in range(l, M + 1, l):
        res += fwk.sum(x)
    while len(a):
        if a[-1][1] - a[-1][0] <= l:
            fwk.add(a[-1][0], 1)
            fwk.add(a.pop()[1] + 1, -1)
        else:
            break
    print(res)
