class Solution:

    def maxNumEdgesToRemove(self, n, edges):

        def find(i):
            if i != root[i]:
                root[i] = find(root[i])
            return root[i]

        def uni(x, y):
            (x, y) = (find(x), find(y))
            if x == y:
                return False
            root[x] = y
            return True
        root = {i: i for i in range(1, n + 1)}
        (res, a, b) = (0, 0, 0)
        for (t, u, v) in edges:
            if t == 3:
                if uni(u, v):
                    a += 1
                    b += 1
                else:
                    res += 1
        common = root.copy()
        for (t, u, v) in edges:
            if t == 1:
                if uni(u, v):
                    a += 1
                else:
                    res += 1
        root = common
        for (t, u, v) in edges:
            if t == 2:
                if uni(u, v):
                    b += 1
                else:
                    res += 1
        return res if a == b == n - 1 else -1
