class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        m = len(locations)
        dp = [[0] * m for x in range(m)]

        for i in range(m):
            for j in range(m):
                dp[i][j] = abs(locations[i] - locations[j])
            dp[i][i] = 1000

        mod = 10**9 + 7

        @lru_cache(None)
        def helper(idx, fuel) -> int:
            if fuel < 0:
                return 0
            else:
                res = 0
                if idx == finish:
                    res = 1
                for j in range(m):
                    # print(\"from idx: \", idx, \" to: \", j, \"fuel = \", fuel)
                    res += helper(j, fuel - dp[idx][j])
                # print(\"res: \", res)
                return res % mod

        return helper(start, fuel)
