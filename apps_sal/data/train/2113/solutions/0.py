import sys
3


class CumTree:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.count = 0
        if a == b:
            return
        mid = (a + b) // 2
        self.levo = CumTree(a, mid)
        self.desno = CumTree(mid + 1, b)

    def manjsi(self, t):
        if self.a >= t:
            return 0
        if self.b < t:
            return self.count
        return self.levo.manjsi(t) + self.desno.manjsi(t)

    def vstavi(self, t):
        if self.a <= t <= self.b:
            self.count += 1
            if self.a == self.b:
                return
            self.levo.vstavi(t)
            self.desno.vstavi(t)


n = int(sys.stdin.readline())
p = [int(x) for x in sys.stdin.readline().strip().split()]

ct = CumTree(1, 4096)

vsota = 0
while len(p) > 0:
    x = p.pop()
    vsota += ct.manjsi(x)
    ct.vstavi(x)

k, d = vsota // 2, vsota % 2
print("%f" % (4 * k + d))
