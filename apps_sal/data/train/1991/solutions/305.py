class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        self.memo = {}
        
        return self.dfs(start, finish, fuel, locations) % (10**9 + 7)
    
    def dfs(self, curr_location, finish, curr_fuel, locations):
        if (curr_location, curr_fuel) in self.memo:
            return self.memo[(curr_location, curr_fuel)]
        if curr_fuel < 0:
            return 0
        
        ways = 1 if curr_location == finish else 0
        
        for i in range(len(locations)):
            if i == curr_location:
                continue
            ways += self.dfs(i, finish, curr_fuel - abs(locations[curr_location]-locations[i]), locations)
        
        self.memo[(curr_location, curr_fuel)] = ways
        
        return ways

