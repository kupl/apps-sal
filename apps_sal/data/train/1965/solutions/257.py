class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

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
