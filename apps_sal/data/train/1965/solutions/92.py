class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        res = 0

        type3 = self.getEdges(edges, 3)
        redudant_edges = self.findRedudantEdges(type3, n + 1)
        res += len(redudant_edges)

        type3 = list(set(type3) - set(redudant_edges))

        type1 = type3 + self.getEdges(edges, 1)
        redudant_edges = self.findRedudantEdges(type1, n + 1)
        if len(type1) - len(redudant_edges) != n - 1:
            return -1

        res += len(redudant_edges)

        type2 = type3 + self.getEdges(edges, 2)
        redudant_edges = self.findRedudantEdges(type2, n + 1)
        if len(type2) - len(redudant_edges) != n - 1:
            return -1

        res += len(redudant_edges)

        return res

    def findRedudantEdges(self, edges, n):
        res = []
        parents = [i for i in range(n)]

        def findParent(a):
            if a != parents[a]:
                parents[a] = findParent(parents[a])

            return parents[a]

        for u, v in edges:
            pu = findParent(u)
            pv = findParent(v)
            if pu == pv:
                res.append((u, v))
            else:
                parents[pu] = pv

        return res

    def getEdges(self, edges, type_num):
        return [(u, v) for t, u, v in edges if t == type_num]
