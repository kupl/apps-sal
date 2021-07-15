class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10 ** 9 + 7
        
        @functools.lru_cache(None)
        def run(c, f):
            res = 0
            if c == finish:
                res += 1
            if f > 0:
                for i in range(len(locations)):
                    if i != c and abs(locations[c]-locations[i]) <= f:
                        res += run(i, f - abs(locations[c]-locations[i])) % MOD
            return res % MOD
        
        return run(start, fuel)
                    

