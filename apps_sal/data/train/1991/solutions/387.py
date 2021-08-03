class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        # place,fuel: times, fuel
        start_val, finish_val = locations[start], locations[finish]
        locations.sort()
        start, finish = bisect.bisect_left(locations, start_val), bisect.bisect_left(locations, finish_val)
        res = 0
        n = len(locations)
        # dp[i][k] means used i fuel end with k
        dp = [[0] * (n) for i in range(fuel + 1)]
        dp[0][start] = 1
        for i in range(0, fuel + 1):
            for j in range(n):
                p = locations[j]
                indl, indr = bisect.bisect_left(locations, p - (fuel - i)), bisect.bisect_right(locations, p + (fuel - i))
                for k in range(indl, indr):
                    if k == j:
                        continue
                    dis = abs(locations[k] - p)
                    dp[dis + i][k] += dp[i][j]
        for i in range(fuel + 1):
            res += dp[i][finish]
        return res % (10**9 + 7)
