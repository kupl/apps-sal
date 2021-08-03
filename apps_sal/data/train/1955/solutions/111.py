class UnionFind(object):
    def __init__(self, n):
        self._parent = [0] * n
        self._size = [1] * n
        self.count = n
        for i in range(n):
            self._parent[i] = i

    def union(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)
        if rootp == rootq:
            return
        self.count -= 1
        if self._size[rootp] > self._size[rootq]:
            self._size[rootp] += self._size[rootq]
            self._parent[rootq] = self._parent[q] = rootp
        else:
            self._size[rootq] += self._size[rootp]
            self._parent[rootp] = self._parent[p] = rootq

    def find(self, n):
        while self._parent[n] != n:
            self._parent[n] = self._parent[self._parent[n]]
            n = self._parent[n]
        return n

    def connected(self, p, q):
        return self.find(p) == self.find(q)


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        N = len(s)
        if N < 2:
            return s
        uf = UnionFind(N)
        for pair in pairs:
            uf.union(pair[0], pair[1])

        dict = defaultdict(list)
        for i in range(N):
            r = uf.find(i)
            dict[r].append(i)

        res = [' '] * N
        for lst in list(dict.values()):
            lst.sort()
            subs = ''
            for idx in lst:
                subs += s[idx]
            s2 = sorted(subs)
            i2 = 0
            for idx in lst:
                res[idx] = s2[i2]
                i2 += 1
        return ''.join(res)
