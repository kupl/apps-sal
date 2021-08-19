class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        for edge in edges:
            edge[1] -= 1
            edge[2] -= 1
        blueUset = self.Uset(n)
        blueUsed = self.countUsed(n, [(edge[1], edge[2]) for edge in edges if edge[0] == 3], blueUset)
        for i in range(0, n):
            blueUset.find(i)
        redUset = self.Uset(n)
        redUset.parents = blueUset.parents[:]
        redUset.gCounts = blueUset.gCounts
        redUsed = self.countUsed(n, [(edge[1], edge[2]) for edge in edges if edge[0] == 1], redUset)
        if redUset.gCounts > 1:
            return -1
        greenUset = self.Uset(n)
        greenUset.parents = blueUset.parents[:]
        greenUset.gCounts = blueUset.gCounts
        greenUsed = self.countUsed(n, [(edge[1], edge[2]) for edge in edges if edge[0] == 2], greenUset)
        if greenUset.gCounts > 1:
            return -1
        return len(edges) - len(blueUsed) - len(redUsed) - len(greenUsed)

    def countUsed(self, n, edges, uset):
        usedEdges = []
        for edge in edges:
            u = edge[0]
            v = edge[1]
            if uset.find(u) != uset.find(v):
                usedEdges.append(edge)
                uset.union(u, v)
        return usedEdges

    class Uset:

        def __init__(self, n):
            self.parents = [i for i in range(0, n)]
            self.gCounts = n

        def find(self, x):
            if self.parents[x] != x:
                self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

        def union(self, x, y):
            px = self.find(x)
            py = self.find(y)
            if px != py:
                self.parents[px] = py
                self.gCounts -= 1
            return
