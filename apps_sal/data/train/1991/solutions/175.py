class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        fuelReduce = lambda x, y: abs(x - y)

        @lru_cache(None)
        def dfs(city, fuel):
            if fuel < 0:
                return 0
            ans = 0
            if city == finish:
                ans = ans + 1
            for next in range(len(locations)):
                if city != next:
                    ans = ans + dfs(next, fuel - fuelReduce(locations[city], locations[next]))
            return ans
        return dfs(start, fuel) % (10 ** 9 + 7)


