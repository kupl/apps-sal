class Solution:

    def countRoutes(self, locations, start: int, finish: int, fuel: int) -> int:

        @lru_cache(maxsize=None)
        def rec(start, finish, fuel):
            if fuel < 0:
                return 0
            if start == finish:
                res = 1
                for j in range(len(locations)):
                    if j != start:
                        res += rec(j, finish, fuel - abs(locations[start] - locations[j]))
                return res
            totalCounts = 0
            for j in range(len(locations)):
                if j != start:
                    totalCounts += rec(j, finish, fuel - abs(locations[start] - locations[j]))
            return totalCounts
        return rec(start, finish, fuel) % (10 ** 9 + 7)
