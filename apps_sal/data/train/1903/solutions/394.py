class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        l = len(points)
        if l < 2:
            return 0
        comps = [i for i in range(l)]

        def comp(v):
            return v if comps[v] == v else comp(comps[v])

        def join_comp(comp1, comp2):
            for i in range(l):
                if comps[i] == comp1:
                    comps[i] = comp2
        edges = []
        for i in range(l):
            for j in range(i + 1, l):
                edges.append((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j))
        edges.sort()
        out = 0
        edge_count = l - 1
        for edge in edges:
            comp1 = comp(edge[1])
            comp2 = comp(edge[2])
            if comp1 != comp2:
                out += edge[0]
                join_comp(comp2, comp1)
                edge_count -= 1
                if not edge_count:
                    break
        return out
