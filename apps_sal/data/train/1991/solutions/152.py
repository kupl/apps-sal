class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        if abs(locations[start]-locations[finish])>fuel: return 0
        lc = len(locations)
        mod = 10**9+7
        @lru_cache(None)
        def rec_dp(s,e,rem):
            
            if rem<0 or abs(locations[s]-locations[e])>rem:
                return 0
            if s==e and rem==0: return 1
            re = 0 if s!=e else 1
            for i in range(lc):
                if i!=s:
                    used = abs(locations[s]-locations[i])
                    re+=rec_dp(i,e,rem-used)
            return re%mod
        
        return rec_dp(start,finish,fuel)
