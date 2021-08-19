from math import log2, ceil


class SegTree:
    #####単位元######
    ide_ele = 0

    def __init__(self, init_val):
        n = len(init_val)
        self.num = 2**ceil(log2(n))
        self.seg = [self.ide_ele] * (2 * self.num - 1)

        for i in range(n):
            self.seg[i + self.num - 1] = init_val[i]

        # built
        for i in range(self.num - 2, -1, -1):
            self.seg[i] = self.segfunc(self.seg[2 * i + 1], self.seg[2 * i + 2])

    #####segfunc######
    def segfunc(self, x, y):
        return x | y

    def update(self, k, x):
        k += self.num - 1
        self.seg[k] = x
        while k:
            k = (k - 1) // 2
            self.seg[k] = self.segfunc(self.seg[k * 2 + 1], self.seg[k * 2 + 2])

    def query(self, a, b, k, l, r):
        if r <= a or b <= l:
            return self.ide_ele
        if a <= l and r <= b:
            return self.seg[k]
        else:
            vl = self.query(a, b, k * 2 + 1, l, (l + r) // 2)
            vr = self.query(a, b, k * 2 + 2, (l + r) // 2, r)
            return self.segfunc(vl, vr)


N = int(input())
S = input()
Q = int(input())

li = [1 << (ord(s) - ord('a')) for s in S]
seg_tree = SegTree(li)
ans = []
for _ in range(Q):
    i, l, r = input().split()
    i = int(i)
    l = int(l)
    if i == 1:
        seg_tree.update(l - 1, 1 << (ord(r) - ord('a')))
    else:
        r = int(r)
        num = seg_tree.query(l - 1, r, 0, 0, seg_tree.num)
        ans.append(bin(num).count('1'))

for a in ans:
    print(a)
