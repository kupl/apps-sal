class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 10 ** 9 + 7
        n = len(locations)
        
        @lru_cache(None)
        def dfs(start, fuel):
            cnt = 0
            if start == finish:
                cnt += 1
            
            for i in range(n):
                if i == start:
                    continue
                cost = abs(locations[i] - locations[start])
                if cost <= fuel:
                    cnt += dfs(i, fuel - cost)
            
            return cnt % mod
                    
        return dfs(start, fuel)

