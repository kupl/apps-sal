class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        q = [(start,fuel)]
        res = 0
        if start == finish:
            res += 1
        next_q = []
        
        @lru_cache(None)
        def dp(cur_start, fuel):
            # if cur_start == finish:
            #     return 0
            
            res = 0
            for l in range(len(locations)):
                left_fuel = fuel - abs(locations[l]-locations[cur_start])
                if l != cur_start and left_fuel >= 0:
                    if l == finish:
                        res += 1
                    if left_fuel > 0:
                        res += dp(l, left_fuel)
            return res
        res += dp(start, fuel)  
        return res % (10**9 +7)
