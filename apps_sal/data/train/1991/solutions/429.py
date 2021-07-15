class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        count = 0
        mod = 10**9+7
        n = len(locations)
        import functools
        @functools.lru_cache(None)
        def DFS(cur_city,cur_fuel):
            if cur_fuel < abs(locations[cur_city]-locations[finish]):
                return 0
            if cur_city == finish:
                c = 1
            else:
                c = 0
                
            for nxt in range(n):
                if nxt == cur_city or cur_fuel < abs(locations[cur_city]-locations[nxt]) :
                    continue
                else:
                    c += DFS(nxt,cur_fuel - abs(locations[cur_city]-locations[nxt]))
            return c % mod
        
        return DFS(start,fuel) % mod
                    

