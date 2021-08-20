class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, totalFuel: int) -> int:
        n = len(locations)
        mod = int(1000000000.0 + 7)
        dp = [[-1] * (totalFuel + 1) for i in range(n)]

        def getNums(current, fuel):
            nonlocal dp, n, finish, start, mod
            if fuel == 0:
                if current == finish:
                    return 1
                return 0
            if dp[current][fuel] > -1:
                return dp[current][fuel]
            ans = 0
            if current == finish:
                ans = 1
            for i in range(n):
                if i != current and abs(locations[current] - locations[i]) <= fuel:
                    ans = (ans + getNums(i, fuel - abs(locations[current] - locations[i]))) % mod
            dp[current][fuel] = ans
            return dp[current][fuel]
        return getNums(start, totalFuel) % mod
