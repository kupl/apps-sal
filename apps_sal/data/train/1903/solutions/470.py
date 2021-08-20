class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        parents = [i for i in range(n)]

        def ufind(node):
            nonlocal parents
            if parents[node] == node:
                return node
            parents[node] = ufind(parents[node])
            return parents[node]

        def union(node1, node2):
            p1 = ufind(node1)
            p2 = ufind(node2)
            if p1 != p2:
                parents[p2] = p1

        def MST(edges):
            nonlocal n
            edges.sort(key=lambda x: x[2])
            ans = 0
            for i in edges:
                p1 = ufind(i[0])
                p2 = ufind(i[1])
                if p1 != p2:
                    ans += i[2]
                    union(p1, p2)
            return ans
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                edges.append((i, j, abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])))
        return MST(edges)
