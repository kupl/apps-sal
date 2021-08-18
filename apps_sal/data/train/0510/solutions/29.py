class SegmentTree(object):
    def __init__(self, sequence, function, identity):
        N = len(sequence)
        self.length = (1 << (N - 1)).bit_length()
        self.function = function
        self.data = [identity] * (self.length << 1)
        self.identity = identity
        for i in range(N):
            self.data[i + self.length - 1] = sequence[i]
        for i in range(self.length - 2, -1, -1):
            self.data[i] = self.function(self.data[(i << 1) + 1], self.data[(i << 1) + 2])

    def update(self, idx, x):
        idx += self.length - 1
        self.data[idx] = x
        while idx:
            idx = (idx - 1) >> 1
            self.data[idx] = self.function(self.data[(idx << 1) + 1], self.data[(idx << 1) + 2])

    def query(self, p, q):
        if q <= p:
            return self.identity
        p += self.length - 1
        q += self.length - 2
        res = self.identity
        while q - p > 1:
            if not p & 1:
                res = self.function(res, self.data[p])
            if q & 1:
                res = self.function(res, self.data[q])
                q -= 1
            p >>= 1
            q = (q - 1) >> 1
        return self.function(res, self.data[p]) if p == q else self.function(self.function(res, self.data[p]), self.data[q])


def popcount(n):
    n = (n & 0x5555555555555555) + ((n & 0xAAAAAAAAAAAAAAAA) >> 1)
    n = (n & 0x3333333333333333) + ((n & 0xCCCCCCCCCCCCCCCC) >> 2)
    n = (n & 0x0F0F0F0F0F0F0F0F) + ((n & 0xF0F0F0F0F0F0F0F0) >> 4)
    n = (n & 0x00FF00FF00FF00FF) + ((n & 0xFF00FF00FF00FF00) >> 8)
    n = (n & 0x0000FFFF0000FFFF) + ((n & 0xFFFF0000FFFF0000) >> 16)
    n = (n & 0x00000000FFFFFFFF) + ((n & 0xFFFFFFFF00000000) >> 32)
    return n


N = int(input())
S = input()
atoi = {chr(ord("a") + d): 1 << d for d in range(26)}
data = [atoi[c] for c in (S)]
seg_tree = SegmentTree(data, lambda a, b: a | b, 0)
Q = int(input())
for _ in range(Q):
    q, a, b = input().split()
    if q == "1":
        idx = int(a) - 1
        seg_tree.update(idx, atoi[b])
    else:
        print(popcount(seg_tree.query(int(a) - 1, int(b))))
