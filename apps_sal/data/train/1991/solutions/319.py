class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)

        @lru_cache(None)
        def dfs(l, f):
            return sum(dfs(i, f - abs(locations[i] - locations[l])) for i in range(n) if i != l
                       and abs(locations[i] - locations[l]) <= f) + (1 if l == finish else 0)

        return dfs(start, fuel) % (10 ** 9 + 7)
