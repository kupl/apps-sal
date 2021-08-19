class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        costs = []
        for i in range(len(points)):
            (xi, yi) = points[i]
            for j in range(i + 1, len(points)):
                (xj, yj) = points[j]
                costs.append([abs(xi - xj) + abs(yi - yj), i, j])
        costs = sorted(costs)
        fathers = {t: t for t in range(len(points))}

        def get_father(n):
            while not fathers[n] == fathers[fathers[n]]:
                fathers[n] = fathers[fathers[n]]
            return fathers[n]
        to_ret = 0
        for t in costs:
            (ct, pi, pj) = t
            if get_father(pi) == get_father(pj):
                continue
            fathers[get_father(pj)] = get_father(pi)
            to_ret += ct
        return to_ret
