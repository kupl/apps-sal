class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        @lru_cache(None)
        def fn(n, x): 
            \"\"\"Return all possible routes from n to finish with x fuel.\"\"\"
            
            if x < 0:
                return 0
            ans = 0
            if n == finish:
                ans += 1
            
            for i in range(len(locations)):
                if i != n:
                    ans += fn(i, x - (abs(locations[n] - locations[i])))
            return ans
        return fn(start, fuel) % 1_000_000_007

