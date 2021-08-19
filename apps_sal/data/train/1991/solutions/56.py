class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        self.MOD = 10 ** 9 + 7

        @functools.lru_cache(None)
        def dfs(i, left):
            if left < 0:
                return 0
            ret = 1 * (i == finish)
            return (sum((dfs(j, left - abs(locations[j] - locations[i])) for j in range(len(locations)) if i != j)) + ret) % self.MOD
        return dfs(start, fuel)
