from math import log
_ = input()
x = [int(i) for i in input().split()]

res = []


class SegmentTree(object):

    def __init__(self, nums):
        self.arr = nums
        self.l = len(nums)
        self.tree = [0] * self.l + nums
        for i in range(self.l - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    def update(self, i, val):
        n = self.l + i
        self.tree[n] = val
        while n > 1:
            self.tree[n >> 1] = self.tree[n] + self.tree[n ^ 1]
            n >>= 1

    def query(self, i, j):
        m = self.l + i
        n = self.l + j
        res = 0
        while m <= n:
            if m & 1:
                res += self.tree[m]
                m += 1
            m >>= 1
            if n & 1 == 0:
                res += self.tree[n]
                n -= 1
            n >>= 1
        return res


tree = SegmentTree(list(range(1, len(x) + 1)))
org = len(x)
while x:
    q = x.pop()

    lo = 0
    hi = org - 1

    while lo < hi:
        mid = (lo + hi) // 2
        # print(lo, hi, mid)
        sm = tree.query(0, mid)
        # print(sm, mid)
        if sm > q:
            hi = mid
        else:
            lo = mid + 1
    # print(tree.arr, lo, hi)
    idx = tree.arr[lo]
    # print(idx)
    tree.update(lo, 0)
    res.append(idx)

print(' '.join(str(i) for i in res[::-1]))
