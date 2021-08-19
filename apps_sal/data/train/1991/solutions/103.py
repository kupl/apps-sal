class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = [[-1] * (fuel + 1) for _ in range(len(locations))]

        def f(cur, cur_fuel):
            if dp[cur][cur_fuel] != -1:
                return dp[cur][cur_fuel]
            total = 1 if cur == finish else 0
            for (i, location) in enumerate(locations):
                if i == cur:
                    continue
                dist = abs(locations[i] - locations[cur])
                if dist <= cur_fuel:
                    total += f(i, cur_fuel - dist)
            dp[cur][cur_fuel] = total
            return total
        return f(start, fuel) % 1000000007
