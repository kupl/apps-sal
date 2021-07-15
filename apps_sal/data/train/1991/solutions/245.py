class Solution:
    
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        memo = {}
        return self.dp(locations, start, finish, fuel, memo)
        
    def dp(self, locations, i, finish, fuel, memo) -> int:
        # ran out of fuel return no possible routes to this location
        if fuel < 0:
            return 0
        
        if (i, fuel) in memo:
            return memo[(i, fuel)]
        
        res = 0
        
        # if we have successfully traversed to the finish, we have found a route
        if i == finish:
            res += 1
        
        for j in range(len(locations)):
            # skip the current location we're at
            if i == j:
                continue
            
            # visit all other locations, subtracting the fuel we used to get here
            res += self.dp(locations, j, finish, fuel - abs(locations[i] - locations[j]), memo)
        
        memo[(i, fuel)] = res % (10 ** 9 + 7)
        return memo[(i, fuel)]

