from heapq import heappop, heappush
n = int(input())
p = [int(x) for x in input().split()]


class SegmentTree:  # 0-indexed
    def __init__(self, array, operation=min, identity=10**30):
        self.identity = identity
        self.n = len(array)
        self.N = 1 << (self.n - 1).bit_length()
        self.tree = [self.identity] * 2 * self.N
        self.opr = operation
        for i in range(self.n):
            self.tree[i + self.N - 1] = array[i]
        for i in range(self.N - 2, -1, -1):
            self.tree[i] = self.opr(self.tree[2 * i + 1], self.tree[2 * i + 2])

    def values(self):
        return self.tree[self.N - 1:]

    def update(self, k, x):
        k += self.N - 1
        self.tree[k] = x
        while k + 1:
            k = (k - 1) // 2
            self.tree[k] = self.opr(self.tree[k * 2 + 1], self.tree[k * 2 + 2])

    def query(self, p, q):  # [p,q)
        if q <= p:
            print("Oops!  That was no valid number.  Try again...")
            return
        p += self.N - 1
        q += self.N - 2
        res = self.identity
        while q - p > 1:
            if p & 1 == 0:
                res = self.opr(res, self.tree[p])
            if q & 1 == 1:
                res = self.opr(res, self.tree[q])
                q -= 1
            p = p // 2
            q = (q - 1) // 2
        if p == q:
            res = self.opr(res, self.tree[p])
        else:
            res = self.opr(self.opr(res, self.tree[p]), self.tree[q])
        return res


ind = [0] * (n + 1)
Odd = SegmentTree([10**30] * n)
Even = SegmentTree([10**30] * n)

for i in range(n):
    ind[p[i]] = i
    if i % 2 == 0:
        Even.update(i, p[i])
    else:
        Odd.update(i, p[i])

cand = []
heappush(cand, (Even.query(0, n), 0, n, True))

q = []
while len(q) < n:
    first, l, r, is_even = heappop(cand)
    if is_even:
        second = Odd.query(ind[first] + 1, r)
        q.extend([first, second])
        if l < ind[first]:
            heappush(cand, (Even.query(l, ind[first]), l, ind[first], True))
        if ind[first] + 1 < ind[second]:
            heappush(
                cand, (Odd.query(ind[first] + 1, ind[second]), ind[first] + 1, ind[second], False))
        if ind[second] + 1 < r:
            heappush(
                cand, (Even.query(ind[second], r), ind[second] + 1, r, True))
    else:
        second = Even.query(ind[first] + 1, r)
        q.extend([first, second])
        if l < ind[first]:
            heappush(cand, (Odd.query(l, ind[first]), l, ind[first], False))
        if ind[first] + 1 < ind[second]:
            heappush(
                cand, (Even.query(ind[first] + 1, ind[second]), ind[first] + 1, ind[second], True))
        if ind[second] + 1 < r:
            heappush(
                cand, (Odd.query(ind[second], r), ind[second] + 1, r, False))

print((*q))
