class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        @lru_cache(None)
        def dfs(start, finish, fuel):
            if fuel < 0:
                return 0

            routes = 1 if start == finish else 0
            for i, location in enumerate(locations):
                if i == start:
                    continue

                routes += dfs(i, finish, fuel - abs(locations[i] - locations[start]))

            return routes

        return dfs(start, finish, fuel) % (10**9 + 7)
