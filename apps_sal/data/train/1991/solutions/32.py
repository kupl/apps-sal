class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        # n = position, x = fuel
        @lru_cache(None)
        def helper(n, x): 
            \"\"\"Return all possible routes from n to finish with x fuel.\"\"\"
            if x < 0: 
                return 0
            res = 0
            if n == finish:
                res += 1
            for next_position in range(len(locations)): 
                if next_position != n: 
                    res += helper(next_position, x-abs(locations[n] - locations[next_position]))
            return res
        
        return helper(start, fuel) % (10**9 + 7)
