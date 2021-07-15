class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        start_pos = locations[start]
        finish_pos = locations[finish]
        
        locations.sort()
        for i,location in enumerate(locations):
            if location == start_pos:
                start = i
            if location == finish_pos:
                finish = i
        print(locations)
        print((start, finish, fuel))
                
        @lru_cache(None)
        def dfs(i,j,f):
            if f < 0:
                return 0
            if abs(locations[i] - locations[j]) > f:
                return 0
            
            l = locations[i] - f
            r = locations[i] + f
            li = bisect.bisect_left(locations,  l)
            ri = bisect.bisect_right(locations, r)
            
            ans = 1 if i == j else 0
            for k in range(li, ri):
                if k != i:
                    ans += dfs(k, j, f - abs(locations[i] - locations[k]))
            return ans
        
        return dfs(start, finish, fuel) % (10 ** 9 + 7)

