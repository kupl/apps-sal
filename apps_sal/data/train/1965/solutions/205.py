class DAU:

    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        (pr, qr) = (self.find(p), self.find(q))
        if pr == qr:
            return False
        else:
            self.parent[pr] = qr
            return True


class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        (ufA, ufB, ufAB) = (DAU(n), DAU(n), DAU(n))
        usefulAB = 0
        for edge in edges:
            t = edge[0]
            x = edge[1]
            y = edge[2]
            if t == 1:
                ufA.union(x - 1, y - 1)
            elif t == 2:
                ufB.union(x - 1, y - 1)
            else:
                ufA.union(x - 1, y - 1)
                ufB.union(x - 1, y - 1)
                usefulAB += ufAB.union(x - 1, y - 1)
        if len([i for i in range(n) if ufA.parent[i] == i]) > 1 or len([i for i in range(n) if ufB.parent[i] == i]) > 1:
            return -1
        return len(edges) - (2 * (n - 1) - usefulAB)
