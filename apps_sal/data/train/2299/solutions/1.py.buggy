

from heapq import heappop, heappush


class SegmentTree():
    def __init__(self, size, f=lambda x, y: x + y, default=0):
        self.size = pow(2, (size - 1).bit_length())
        self.f = f
        self.default = default
        self.data = [default] * (self.size * 2)

    def update(self, i, x):
        i += self.size
        self.data[i] = x
        while i:
            i >>= 1
            self.data[i] = self.f(self.data[i * 2], self.data[i * 2 + 1])
    # 区間[l,r)へのクエリ

    def query(self, l, r):
        l, r = l + self.size, r + self.size
        lret, rret = self.default, self.default
        while l < r:
            if l & 1:
                lret = self.f(self.data[l], lret)
                l += 1
            if r & 1:
                r -= 1
                rret = self.f(self.data[r], rret)
            l >>= 1
            r >>= 1
        return self.f(lret, rret)

    def get(self, i):
        return self.data[self.size + i]

    def add(self, i, x):
        self.update(i, self.get(i) + x)


def main1(n, p):
    d = {}
    st0 = SegmentTree(n, min, n + 1)
    st1 = SegmentTree(n, min, n + 1)
    for i, x in enumerate(p):
        d[x] = i
        if i % 2 == 0:
            st0.update(i, x)
        else:
            st1.update(i, x)

    def func(l, r):
        if l % 2 == 0:
            v0 = st0.query(l, r)
            i0 = d[v0]
            v1 = st1.query(i0, r)
        else:
            v0 = st1.query(l, r)
            i0 = d[v0]
            v1 = st0.query(i0, r)
        return v0, v1, l, r
    # 区間ごとの辞書順最小先頭を管理：[[v0,v1],[v0,v1,...]
    ary = []
    heappush(ary, func(0, n))
    ret = []
    for _ in range(n // 2):
        v0, v1, l, r = heappop(ary)
        ret.append(v0)
        ret.append(v1)
        i0 = d[v0]
        i1 = d[v1]
        if i0 != l:
            heappush(ary, func(l, i0))
        if i0 + 1 != i1:
            heappush(ary, func(i0 + 1, i1))
        if i1 + 1 != r:
            heappush(ary, func(i1 + 1, r))
    return ret


def __starting_point():
    n = int(input())
    p = list(map(int, input().split()))
    ret1 = main1(n, p.copy())
    print((*ret1))


__starting_point()
