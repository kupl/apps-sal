class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        def cost(a, b):
            return abs(locations[a] - locations[b])
        N = len(locations)

        @lru_cache(None)
        def dfs(curr, fuel):
            if fuel < 0:
                return 0
            ans = 1 if curr == finish else 0
            return ans + sum((dfs(i, fuel - cost(curr, i)) for i in range(N) if i != curr))
        return dfs(start, fuel) % (10 ** 9 + 7)
