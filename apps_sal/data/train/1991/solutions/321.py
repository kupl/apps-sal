import sys
sys.setrecursionlimit(1000)

class Solution:
    def rec(self, p, f):
        if f<0:
            return 0
        
        if self.memo[p][f]!=-1:
            return self.memo[p][f]
    
        res = 1 if p==self.start else 0
        
        for i in range(len(self.locations)):
            if i==p:
                continue
            
            res += self.rec(i, f-abs(self.locations[p]-self.locations[i]))
            res %= self.MOD
        
        self.memo[p][f] = res
        return res
        
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        self.locations = locations
        self.start = start
        self.memo = [[-1]*(fuel+1) for _ in range(len(locations))]
        self.MOD = 10**9+7
        return self.rec(finish, fuel)
