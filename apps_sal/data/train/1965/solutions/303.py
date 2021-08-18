class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def find(i):
            if i != root[i]:
                root[i] = find(root[i])
            return root[i]

        def uni(x, y):
            x, y = find(x), find(y)
            if x == y:
                return 0
            root[x] = y
            return 1

        res, e1, e2 = [0], [0], [0]

        t1, t2, t3 = [], [], []
        for i in range(len(edges)):
            t = edges[i][0]
            if t == 1:
                t1.append(i)
            elif t == 2:
                t2.append(i)
            elif t == 3:
                t3.append(i)

        root = [i for i in range(n + 1)]
        for k in t3:
            t, i, j = edges[k]
            if uni(i, j):
                e1[0] += 1
                e2[0] += 1
            else:
                res[0] += 1
        root0 = root[:]

        for k in t1:
            t, i, j = edges[k]
            if uni(i, j):
                e1[0] += 1
            else:
                res[0] += 1

        root = root0
        for k in t2:
            t, i, j = edges[k]
            if uni(i, j):
                e2[0] += 1
            else:
                res[0] += 1

        return res[0] if e1[0] == e2[0] == n - 1 else -1
