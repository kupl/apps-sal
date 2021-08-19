class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        costs = []
        ans = 0
        for (i, node_x) in enumerate(points):
            for (j, node_y) in enumerate(points):
                if i != j:
                    costs.append((abs(node_x[0] - node_y[0]) + abs(node_x[1] - node_y[1]), i, j))
        costs.sort()

        def get_fa(i):
            if fa[i] != i:
                fa[i] = get_fa(fa[i])
            return fa[i]
        fa = list(range(len(points)))
        count = 0
        for (v, i, j) in costs:
            if get_fa(i) != get_fa(j):
                ans += v
                fa[fa[i]] = fa[j]
                count += 1
                if count == len(points) - 1:
                    return ans
        return ans
