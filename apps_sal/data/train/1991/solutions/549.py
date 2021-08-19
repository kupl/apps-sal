class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        @lru_cache(None)
        def dfs(i: int, f: int) -> int:
            ans = 1 if i == finish else 0
            for j in range(len(locations)):
                diff = abs(locations[j] - locations[i])
                if j == i:
                    continue
                elif diff <= f:
                    #                    if j==finish:
                    #                        ans += 1
                    ans += dfs(j, f - diff)
            return ans

        return dfs(start, fuel) % (10**9 + 7)
