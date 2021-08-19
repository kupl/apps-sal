class Solution:

    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        m = len(costs)
        n = m // 2
        f = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(min(n, i) + 1):
                f[i][j] = math.inf
                if j > 0:
                    f[i][j] = costs[i - 1][0] + f[i - 1][j - 1]
                if i - j > 0:
                    f[i][j] = min(f[i][j], costs[i - 1][1] + f[i - 1][j])
        return f[m][n]
