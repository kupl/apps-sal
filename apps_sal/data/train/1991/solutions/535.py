class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        @lru_cache(None)
        def dfs(i, f):
            ans = i == finish
            for j in range(len(locations)):
                if j != i:
                    delta = abs(locations[i] - locations[j])
                    if delta <= f:
                        ans += dfs(j, f - delta)
            return ans
        return dfs(start, fuel) % (10 ** 9 + 7)
