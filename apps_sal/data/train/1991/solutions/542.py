class Solution:
    def countRoutes(self, a: List[int], start: int, end: int, startfuel: int) -> int:
        
        MOD = 10**9 + 7
        
        start = a[start]
        end = a[end]
        
        @lru_cache(None)
        def recurse(pos, fuel):
            
            if fuel < 0:
                return 0
            
            ret = pos == end
            
            for POS in a:
                
                if POS == pos:
                    continue
                
                ret += recurse(POS, fuel - abs(POS - pos))
                
            return ret % MOD
        
        return recurse(start, startfuel)
        
        \"\"\"
        n = len(a)
        
        start = a[start]
        end = a[end]
        
        # dp[pos][fuel]
        
        # n * f * f * n
        
        # hmmm. i feel this will time out?
        
        # i still feel this would time the fuck out.....
        
        # well... lets see, anyways
        
        MOD = 10**9 + 7
        
        ret = 0
        
        cnt = Counter({(start, startfuel): 1})
        
        while cnt:
            
            cnt2 = Counter()
            
            # print(cnt)
            
            for pos, fuel in cnt:
                
                if pos == end:
                    ret += cnt[pos, fuel]
                    ret %= MOD
                    
                for pos2 in a:
                    if pos2 == pos:
                        continue
                    
                    fuel2 = fuel - abs(pos2 - pos)
                    
                    if fuel2 >= 0:
                        cnt2[pos2, fuel2] += cnt[pos, fuel]
                        cnt2[pos2, fuel2] %= MOD
            
            
            cnt = cnt2
        
        return ret
        \"\"\"
            
