from sys import stdin


def bitadd(a, w, bit):

    x = a
    while x <= (len(bit) - 1):
        bit[x] += w
        x += x & (-1 * x)


def bitsum(a, bit):

    ret = 0
    x = a
    while x > 0:
        ret += bit[x]
        x -= x & (-1 * x)
    return ret


class RangeBIT:

    def __init__(self, N, indexed):
        self.bit1 = [0] * (N + 2)
        self.bit2 = [0] * (N + 2)
        self.mode = indexed

    def bitadd(self, a, w, bit):

        x = a
        while x <= (len(bit) - 1):
            bit[x] += w
            x += x & (-1 * x)

    def bitsum(self, a, bit):

        ret = 0
        x = a
        while x > 0:
            ret += bit[x]
            x -= x & (-1 * x)
        return ret

    def add(self, l, r, w):

        l = l + (1 - self.mode)
        r = r + (1 - self.mode)
        self.bitadd(l, -1 * w * l, self.bit1)
        self.bitadd(r, w * r, self.bit1)
        self.bitadd(l, w, self.bit2)
        self.bitadd(r, -1 * w, self.bit2)

    def sum(self, l, r):
        l = l + (1 - self.mode)
        r = r + (1 - self.mode)
        ret = self.bitsum(r, self.bit1) + r * self.bitsum(r, self.bit2)
        ret -= self.bitsum(l, self.bit1) + l * self.bitsum(l, self.bit2)

        return ret


n, q = list(map(int, stdin.readline().split()))
a = list(map(int, stdin.readline().split()))

qs = [[] for i in range(n + 1)]
ans = [None] * q

for loop in range(q):
    x, y = list(map(int, stdin.readline().split()))
    l = x + 1
    r = n - y
    qs[r].append((l, loop))

BIT = [0] * (n + 1)

for r in range(1, n + 1):

    b = r - a[r - 1]

    if b >= 0:

        L = 1
        R = r + 1
        while R - L != 1:
            M = (L + R) // 2

            if bitsum(M, BIT) >= b:
                L = M
            else:
                R = M

        if bitsum(L, BIT) >= b:
            bitadd(1, 1, BIT)
            bitadd(L + 1, -1, BIT)

    for ql, qind in qs[r]:
        ans[qind] = bitsum(ql, BIT)

for i in ans:
    print(i)
