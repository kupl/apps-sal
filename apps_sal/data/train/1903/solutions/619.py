class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        costs = []
        for i in range(len(points)):
            xi, yi = points[i]
            for j in range(i + 1, len(points)):
                xj, yj = points[j]
                costs.append([abs(xi - xj) + abs(yi - yj), i, j])
        costs = sorted(costs)

        fathers = [t for t in range(len(points))]

        def get_father(n):
            while not fathers[n] == fathers[fathers[n]]:
                fathers[n] = fathers[fathers[n]]
            return fathers[n]

        res = 0
        for t in costs:
            dist, i, j = t
            if get_father(i) == get_father(j):
                continue
            fathers[get_father(j)] = get_father(i)
            res += dist
        return res
