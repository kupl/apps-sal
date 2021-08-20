import sys
input = sys.stdin.readline
S = input()
T = input()
q = int(input())
abcd = [list(map(int, input().split())) for i in range(q)]


class SegmentTree:

    def __init__(self, data, op, default):
        N = len(data)
        self.N = N
        self.op = op
        self.default = default
        self.l = 2 ** (N - 1).bit_length()
        self.data = [default] * self.l + data + [default] * (self.l - N)
        for i in range(self.l - 1, 0, -1):
            self.data[i] = op(self.data[2 * i], self.data[2 * i + 1])

    def get_data(self, i=None):
        if i is None:
            return self.data[self.l:self.l + self.N]
        else:
            return self.data[self.l + i]

    def set(self, i, val):
        i += self.l
        self.data[i] = val
        i = i // 2
        while i > 0:
            self.data[i] = self.op(self.data[2 * i], self.data[2 * i + 1])
            i = i // 2

    def get(self, i, j):
        i += self.l
        j += self.l
        s = self.default
        while j - i > 0:
            if i & 1:
                s = self.op(s, self.data[i])
                i += 1
            if j & 1:
                s = self.op(s, self.data[j - 1])
                j -= 1
            (i, j) = (i // 2, j // 2)
        return s


def convert(x):
    return 1 if x == 'A' else 2


nS = list(map(convert, S))
nT = list(map(convert, T))
segS = SegmentTree(nS, lambda x, y: x + y, 0)
segT = SegmentTree(nT, lambda x, y: x + y, 0)
for (a, b, c, d) in abcd:
    rs = segS.get(a - 1, b)
    rt = segT.get(c - 1, d)
    if (rs - rt) % 3 == 0:
        print('YES')
    else:
        print('NO')
