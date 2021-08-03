class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # Union find
        #         def find(i):
        #             if i != root[i]:
        #                 root[i] = find(root[i])
        #             return root[i]

        #         def uni(x, y):
        #             x, y = find(x), find(y)
        #             if x == y: return 0
        #             root[x] = y
        #             return 1

        #         res = e1 = e2 = 0

        #         # Alice and Bob
        #         root = list(range(n + 1))
        #         for t, i, j in edges:
        #             if t == 3:
        #                 if uni(i, j):
        #                     e1 += 1
        #                     e2 += 1
        #                 else:
        #                     res += 1
        #         root0 = root[:]

        #         # only Alice
        #         for t, i, j in edges:
        #             if t == 1:
        #                 if uni(i, j):
        #                     e1 += 1
        #                 else:
        #                     res += 1

        #         # only Bob
        #         root = root0
        #         for t, i, j in edges:
        #             if t == 2:
        #                 if uni(i, j):
        #                     e2 += 1
        #                 else:
        #                     res += 1

        #         return res if e1 == e2 == n - 1 else -1

        def findRoot(a):
            if a != root[a]:
                root[a] = findRoot(root[a])
            return root[a]

        def union(a, b):
            aRoot, bRoot = findRoot(a), findRoot(b)
            if aRoot != bRoot:
                root[aRoot] = bRoot
                return True
            return False

        root = [i for i in range(n + 1)]
        numofEdgesAli, numofEdgesBob, ans = 0, 0, 0
        for t, a, b in edges:
            if t == 3:
                if union(a, b):
                    numofEdgesAli += 1
                    numofEdgesBob += 1
                else:
                    ans += 1
        root0 = root[:]
        for t, a, b in edges:
            if t == 1:
                if union(a, b):
                    numofEdgesAli += 1
                else:
                    ans += 1
        root = root0
        for t, a, b in edges:
            if t == 2:
                if union(a, b):
                    numofEdgesBob += 1
                else:
                    ans += 1
        return ans if numofEdgesAli == numofEdgesBob == n - 1 else -1
