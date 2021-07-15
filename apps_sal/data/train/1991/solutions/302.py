class Solution:
    def solve(self, curr_loc, fuel):
        if fuel < 0:
            return 0
        if (curr_loc, fuel) in self.dp:
            return self.dp[curr_loc, fuel]
        ways = 0
        if curr_loc == self.finish:
            ways += 1
        for i in range(len(self.locations)):
            if i != curr_loc:
                ways += self.solve(i, fuel - abs(self.locations[i]-self.locations[curr_loc]))
        self.dp[curr_loc, fuel] = ways %  self.modz
        return ways
            
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        self.locations = locations
        self.dp = {}
        self.modz = pow(10,9) + 7
        self.finish = finish
        return self.solve(start, fuel) %  self.modz
