class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        self.memo = {}
        self.mod = 10**9 + 7
        return self.helper(start, finish, locations, fuel)
    
    def helper(self, curr, finish, locations, fuel):
        if fuel < 0:
            return 0
        
        if (curr, fuel) in self.memo:
            return self.memo[(curr, fuel)]
        
        res = 1 if curr == finish else 0
        
        for next_i in range(len(locations)):
            if next_i != curr:
                update = abs(locations[next_i] - locations[curr])
                res += self.helper(next_i, finish, locations, fuel-update)
        
        res = res % self.mod
        self.memo[(curr, fuel)] = res 
        return res
