class UnionFind:

    def __init__(self, n):
        self.parentArr = [i for i in range(1 + n)]
        self.groupSize = [1 for i in range(1 + n)]
        self.numGroups = n

    def union(self, i, j):
        (root_i, root_j) = (self.getRoot(i), self.getRoot(j))
        self.numGroups -= 1
        if self.groupSize[root_i] < self.groupSize[root_j]:
            self.parentArr[root_i] = root_j
            self.groupSize[root_j] += self.groupSize[root_i]
        else:
            self.parentArr[root_j] = root_i
            self.groupSize[root_i] += self.groupSize[root_j]

    def getRoot(self, i):
        if self.parentArr[i] == i:
            return i
        else:
            ans = self.getRoot(self.parentArr[i])
            self.parentArr[i] = ans
            return ans


class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges.sort()
        uf_alice = UnionFind(n)
        uf_bob = UnionFind(n)
        ans = 0
        for edge in reversed(edges):
            (edgeType, u, v) = edge
            if edgeType == 3:
                (root_u, root_v) = (uf_alice.getRoot(u), uf_alice.getRoot(v))
                if root_u != root_v:
                    uf_alice.union(u, v)
                    uf_bob.union(u, v)
                    ans += 1
            elif edgeType == 1:
                (root_u, root_v) = (uf_alice.getRoot(u), uf_alice.getRoot(v))
                if root_u != root_v:
                    uf_alice.union(u, v)
                    ans += 1
            else:
                (root_u, root_v) = (uf_bob.getRoot(u), uf_bob.getRoot(v))
                if root_u != root_v:
                    uf_bob.union(u, v)
                    ans += 1
            if uf_alice.numGroups == 1 and uf_bob.numGroups == 1:
                break
        return len(edges) - ans if uf_alice.numGroups == 1 and uf_bob.numGroups == 1 else -1
