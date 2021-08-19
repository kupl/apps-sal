import copy


class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        def find(u):
            if root[u] != u:
                root[u] = find(root[u])
            return root[u]

        def union(u, v):
            (ru, rv) = (find(u), find(v))
            if ru == rv:
                return 0
            root[ru] = root[rv]
            return 1
        root = [i for i in range(n + 1)]
        res = e1 = e2 = 0
        for (t, i, j) in edges:
            if t == 3:
                if union(i, j):
                    e1 += 1
                    e2 += 1
                else:
                    res += 1
        rootCopy = copy.deepcopy(root)
        for (t, i, j) in edges:
            if t == 1:
                if union(i, j):
                    e1 += 1
                else:
                    res += 1
        root = rootCopy
        for (t, i, j) in edges:
            if t == 2:
                if union(i, j):
                    e2 += 1
                else:
                    res += 1
        return res if e1 == n - 1 and e2 == n - 1 else -1
