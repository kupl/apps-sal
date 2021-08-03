import sys
def input(): return sys.stdin.readline().rstrip()


class SegTree:
    X_unit = 0

    def __init__(self, N, X_f=min):
        self.N = N
        self.X = [self.X_unit] * (N + N)
        self.X_f = X_f

    def build(self, seq):
        for i, x in enumerate(seq, self.N):
            self.X[i] = x
        for i in range(self.N - 1, 0, -1):
            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

    def set_val(self, i, x):
        i += self.N
        self.X[i] = x
        while i > 1:
            i >>= 1
            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

    def fold(self, L, R):
        L += self.N
        R += self.N
        vL = self.X_unit
        vR = self.X_unit
        while L < R:
            if L & 1:
                vL = self.X_f(vL, self.X[L])
                L += 1
            if R & 1:
                R -= 1
                vR = self.X_f(self.X[R], vR)
            L >>= 1
            R >>= 1
        return self.X_f(vL, vR)


def orr(x, y):
    return x | y


def main():
    N = int(input())
    S = input()
    S = list(map(lambda c: 2**(ord(c) - ord('a')), list(S)))
    Q = int(input())
    seg = SegTree(N, orr)
    seg.build(S)
    for _ in range(Q):
        num, x, y = input().split()
        if num == '1':
            seg.set_val(int(x) - 1, 2**(ord(y) - ord('a')))
        else:
            bits = seg.fold(int(x) - 1, int(y))
            print(sum(map(int, list(bin(bits))[2:])))


def __starting_point():
    main()


__starting_point()
