class Solution:

    def _root(self, U, a):
        while U[a] != a:
            U[a] = U[U[a]]
            a = U[a]
        return a

    def _union(self, U, a, b):
        ra = self._root(U, a)
        rb = self._root(U, b)
        if ra == rb:
            return False
        U[ra] = rb
        return True

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(key=lambda x: x[0], reverse=True)
        ua = [i for i in range(n + 1)]
        ub = [i for i in range(n + 1)]
        (e1, e2, e3) = (0, 0, 0)
        for (ty, u, v) in edges:
            if ty == 3:
                tmp = self._union(ua, u, v)
                tmp = self._union(ub, u, v) or tmp
                if tmp:
                    e3 += 1
            elif ty == 2:
                if self._union(ub, u, v):
                    e2 += 1
            elif ty == 1:
                if self._union(ua, u, v):
                    e1 += 1
        (ca, cb) = (0, 0)
        for i in range(1, n + 1):
            if ua[i] == i:
                ca += 1
            if ub[i] == i:
                cb += 1
            if ca > 1 or cb > 1:
                return -1
        return len(edges) - e1 - e2 - e3
