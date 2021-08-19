class SegmentTree(object):

    def __init__(self, sequence, function, identity):
        N = len(sequence)
        self.length = (1 << N - 1).bit_length()
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
            idx = idx - 1 >> 1
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
            q = q - 1 >> 1
        return self.function(res, self.data[p]) if p == q else self.function(self.function(res, self.data[p]), self.data[q])


def popcount(n):
    n = (n & 6148914691236517205) + ((n & 12297829382473034410) >> 1)
    n = (n & 3689348814741910323) + ((n & 14757395258967641292) >> 2)
    n = (n & 1085102592571150095) + ((n & 17361641481138401520) >> 4)
    n = (n & 71777214294589695) + ((n & 18374966859414961920) >> 8)
    n = (n & 281470681808895) + ((n & 18446462603027742720) >> 16)
    n = (n & 4294967295) + ((n & 18446744069414584320) >> 32)
    return n


N = int(input())
S = input()
atoi = {chr(ord('a') + d): 1 << d for d in range(26)}
data = [atoi[c] for c in S]
seg_tree = SegmentTree(data, lambda a, b: a | b, 0)
Q = int(input())
for _ in range(Q):
    (q, a, b) = input().split()
    if q == '1':
        idx = int(a) - 1
        seg_tree.update(idx, atoi[b])
    else:
        print(popcount(seg_tree.query(int(a) - 1, int(b))))
