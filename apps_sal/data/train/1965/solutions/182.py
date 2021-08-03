class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]

        e1 = 0
        e2 = 0
        res = 0

        def union(x, y):
            x = find(x)
            y = find(y)
            if x == y:
                return 0
            root[x] = y
            return 1

        root = list(range(n + 1))
        for t, i, j in edges:
            if t == 3:
                if union(i, j):
                    e1 += 1
                    e2 += 1
                else:
                    res += 1
        temp = root[:]

        for t, i, j in edges:
            if t == 1:
                if union(i, j):
                    e1 += 1
                else:
                    res += 1

        root = temp

        for t, i, j in edges:
            if t == 2:
                if union(i, j):
                    e2 += 1
                else:
                    res += 1

        if e1 == n - 1 and e2 == n - 1:
            return res
        else:
            return -1
