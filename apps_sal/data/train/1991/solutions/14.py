
MODNUM = 1000000007

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        
        @lru_cache(None)
        def dp(i, j, f):
            if f <= 0:
                return 0
            
            res = 1 if i != j and abs(locations[i] - locations[j]) <= f else 0
            N = len(locations)
            for k in range(N):
                if k == j:
                    continue
                dkj = abs(locations[k] - locations[j])
                if dkj < f:
                    res = (res + dp(i, k, f - dkj)) % MODNUM
            
            return res
    
        return dp(start, finish, fuel) + (1 if (start == finish) else 0)
