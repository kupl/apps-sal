class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        sets = list(range(len(points)))

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append([d, i, j])

        edges.sort()
        n_edges = 0
        ans = 0
        cur = 0

        def find(i):
            while sets[i] != i:
                i = sets[i]
            return i

        while n_edges != len(sets) - 1:
            d, i, j = edges[cur]
            # print(i, j, sets)
            if find(i) != find(j):
                sets[find(i)] = find(j)
                ans += d
                n_edges += 1
            cur += 1
        return ans
