class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        start_loc = locations[start]
        finish_loc = locations[finish]
        locations.sort()
        start = bisect_left(locations, start_loc)
        finish = bisect_left(locations, finish_loc)

        @lru_cache(None)
        def dp(cur, cur_fuel):
            return total
        dp = [[-1] * (fuel + 1) for _ in range(len(locations))]

        def f(cur, cur_fuel):
            if dp[cur][cur_fuel] != -1:
                return dp[cur][cur_fuel]
            if abs(locations[cur] - locations[finish]) > fuel:
                return 0
            total = 1 if cur == finish else 0
            for i in range(cur + 1, len(locations)):
                dist = locations[i] - locations[cur]
                if dist <= cur_fuel:
                    total += f(i, cur_fuel - dist)
                else:
                    break
            for i in reversed(list(range(0, cur))):
                dist = locations[cur] - locations[i]
                if dist <= cur_fuel:
                    total += f(i, cur_fuel - dist)
                else:
                    break
            dp[cur][cur_fuel] = total
            return total
        return f(start, fuel) % 1000000007
