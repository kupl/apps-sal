class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        self.memo = {}
        return self.dfs(start, finish, fuel, locations) % (10**9 + 7)
    
    def dfs(self, curr_loc, finish, curr_fuel, locations):
        if (curr_loc, curr_fuel) in self.memo:
            return self.memo[(curr_loc, curr_fuel)]
        if curr_fuel < 0:
            return 0
        
        ways = 0 if curr_loc != finish else 1
        
        for i in range(len(locations)):
            if i == curr_loc:
                continue
            ways += self.dfs(i, finish, curr_fuel - abs(locations[i] - locations[curr_loc]), locations)

        self.memo[(curr_loc, curr_fuel)] = ways
        return ways
