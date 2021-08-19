from collections import defaultdict


class UnionFind:

    def __init__(self, n):
        self._id = list(range(n))
        self._sz = [1] * n
        self.cc = n

    def _root(self, i):
        j = i
        while j != self._id[j]:
            self._id[j] = self._id[self._id[j]]
            j = self._id[j]
        return j

    def find(self, p, q):
        return self._root(p) == self._root(q)

    def union(self, p, q):
        i = self._root(p)
        j = self._root(q)
        if i == j:
            return
        if self._sz[i] < self._sz[j]:
            self._id[i] = j
            self._sz[j] += self._sz[i]
        else:
            self._id[j] = i
            self._sz[i] += self._sz[j]
        self.cc -= 1


class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        class1 = UnionFind(n)
        class2 = UnionFind(n)
        for (cat, start, end) in edges:
            graph[cat].append((start - 1, end - 1))
        class1 = UnionFind(n)
        class2 = UnionFind(n)
        ans = 0
        for (start, end) in graph[3]:
            (cur1, cur2) = (class1.cc, class2.cc)
            class1.union(start, end)
            class2.union(start, end)
            if class1.cc == cur1 and class2.cc == cur2:
                ans += 1
        for (start, end) in graph[1]:
            cur1 = class1.cc
            class1.union(start, end)
            if class1.cc == cur1:
                ans += 1
        for (start, end) in graph[2]:
            cur2 = class2.cc
            class2.union(start, end)
            if class2.cc == cur2:
                ans += 1
        if class1.cc == 1 and class2.cc == 1:
            return ans
        else:
            return -1
