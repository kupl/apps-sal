from functools import lru_cache
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        
        @lru_cache(None)
        def dp(j, f):
            # print(j, f)
            summ = 0
            for idx, loc in enumerate(locations):
                if idx == j: continue
                step = abs(loc - locations[j])
                if step < f:
                    if idx == start:    summ += 1
                    summ += dp(idx, f-step)
                elif step == f and idx == start:
                    summ += 1
            return summ
        
        return (dp(finish, fuel)) % (10**9+7) + (1 if start == finish else 0)
