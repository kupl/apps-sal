class Solution:
    def rec(self, locs, cur, finish, fuel, dp):
        if fuel == 0:
            return cur == finish
        
        if (cur, fuel) in dp:
            return dp[(cur, fuel)]
        
        res = cur == finish
        pos = []
        for i in range(len(locs)):
            if i != cur and abs(locs[i]-locs[cur]) <= fuel:
                pos += [(i, fuel-abs(locs[i]-locs[cur]))]
        
        for i in range(len(pos)):
            res += self.rec(locs, pos[i][0], finish, pos[i][1], dp)
        
        dp[(cur, fuel)] = res
        return res
                
    
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = {}
        MOD = 10**9+7
        return self.rec(locations, start, finish, fuel, dp)%MOD
