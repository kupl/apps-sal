class SegmentTree:

    def __init__(self, n, ele=0):
        self.ide_ele = ele
        self.num = 2 ** (n - 1).bit_length()
        self.seg = [self.ide_ele] * 2 * self.num

    def segfunc(self, x, y):
        return x | y

    def init(self, init_val):
        for i in range(len(init_val)):
            self.seg[i + self.num - 1] = init_val[i]
        for i in range(self.num - 2, -1, -1):
            self.seg[i] = self.segfunc(self.seg[2 * i + 1], self.seg[2 * i + 2])

    def update(self, k, x):
        k += self.num - 1
        if self.seg[k] == x:
            return 0
        self.seg[k] = x
        while k:
            k = (k - 1) // 2
            self.seg[k] = self.segfunc(self.seg[k * 2 + 1], self.seg[k * 2 + 2])

    def query(self, p, q):
        if q <= p:
            return self.ide_ele
        p += self.num - 1
        q += self.num - 2
        res = self.ide_ele
        while q - p > 1:
            if p & 1 == 0:
                res = self.segfunc(res, self.seg[p])
            if q & 1 == 1:
                res = self.segfunc(res, self.seg[q])
                q -= 1
            p = p // 2
            q = (q - 1) // 2
        if p == q:
            res = self.segfunc(res, self.seg[p])
        else:
            res = self.segfunc(self.segfunc(res, self.seg[p]), self.seg[q])
        return res


(N, S, Q) = (int(input()), input(), int(input()))
d = {'a': 1, 'b': 2, 'c': 4, 'd': 8, 'e': 16, 'f': 32, 'g': 64, 'h': 128, 'i': 256, 'j': 512, 'k': 1024, 'l': 2048, 'm': 4096, 'n': 8192, 'o': 16384, 'p': 32768, 'q': 65536, 'r': 131072, 's': 262144, 't': 524288, 'u': 1048576, 'v': 2097152, 'w': 4194304, 'x': 8388608, 'y': 16777216, 'z': 33554432}
initial = [d[c] for c in list(S)]
ST = SegmentTree(N)
ST.init(initial)
for _ in range(Q):
    (typ, a, b) = input().split()
    if typ == '1':
        (i, c) = (int(a), d[b])
        ST.update(i - 1, c)
    else:
        (l, r) = (int(a) - 1, int(b))
        x = bin(ST.query(l, r))[2:]
        print(sum(map(int, list(x))))
