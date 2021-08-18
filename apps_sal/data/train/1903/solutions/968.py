class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        edges = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                if i == j:
                    continue
                edges.append([distance(points[i], points[j]), i, j])
        edges.sort()

        fathers = {p: p for p in range(len(points))}

        def find_father(p):
            while fathers[p] != fathers[fathers[p]]:
                fathers[p] = find_father(fathers[p])
            return fathers[p]

        result = 0
        for d, p1, p2 in edges:
            if find_father(p1) == find_father(p2):
                continue
            fathers[find_father(p2)] = find_father(p1)
            result += d

        return result
