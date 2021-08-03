class Solution:
    def maxNumEdgesToRemove(self, n: int, edges) -> int:
        def find(i):
            if root[i] != i:
                root[i] = find(root[i])
            return root[i]

        def union(u, v):
            ru, rv = find(u), find(v)
            if ru == rv:
                return False
            root[ru] = rv
            return True

        root = list(range(n + 1))
        edges_alice, edges_bob, res = 0, 0, 0
        for t, u, v in edges:
            if t == 3:
                if union(u, v):
                    edges_alice += 1
                    edges_bob += 1
                else:
                    res += 1

        root_copy = root[:]  # a copy of connection 3
        for t, u, v in edges:
            if t == 1:
                if union(u, v):
                    edges_alice += 1
                else:
                    res += 1

        root = root_copy
        for t, u, v in edges:
            if t == 2:
                if union(u, v):
                    edges_bob += 1
                else:
                    res += 1
        if edges_alice == n - 1 and edges_bob == n - 1:
            return res
        else:
            return -1
