import sys


class BIT():
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def _add(self, i, val):
        while i > 0:
            self.bit[i] += val
            i -= i & -i

    def get_val(self, i):
        i = i + 1
        s = 0
        while i <= self.n:
            s += self.bit[i]
            i += i & -i
        return s

    def add(self, l, r, val):
        self._add(r, val)
        self._add(l, -val)


input = sys.stdin.readline


t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = a[n // 2:n][::-1]
    a = a[0:n // 2]

    bit = BIT(2 * k + 1)
    bit.add(0, 2 * k + 1, (2 * n // 2))
    for i in range(n // 2):
        ran = [min(a[i] + 1, b[i] + 1), max(a[i] + k + 1, b[i] + k + 1)]
        bit.add(ran[0], ran[1], -1)
        bit.add(a[i] + b[i], a[i] + b[i] + 1, -1)
    print(min([bit.get_val(i) for i in range(2 * k + 1)]))
