from functools import lru_cache
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 10**9 + 7
        @lru_cache(None)
        def dfs(state, remain):
            if remain < 0: return 0
            cnt = 0
            if state == finish:
                cnt += 1
            for next_state, next_loc in enumerate(locations):
                if next_state == state: continue
                cnt += dfs(next_state, remain-abs(locations[state]-next_loc))
            return cnt % mod
        return dfs(start, fuel)

