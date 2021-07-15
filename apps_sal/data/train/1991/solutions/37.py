class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        # Note that my first approach was to use dfs - see my earliest submission
        # It gave correct results, but failed TLE.
        
        # From looking at discussion, it was clear dp works best.
        # Create blank dp grid with [fuel][location]
        # begin at point [starting fuel][starting location] = 1
        # iterate from biggest locations, starting fuel, reducing
        # location by 1 each time, then reducing fuel
        # if you encounter a 0 in dp, ignore it
        # But otherwise, calculate the locations you can move to 
        # -- ignoring moving back to that same location --
        # and in each of those locations, with the reduced fuel amount,
        # add in the value that was in the dp grid that got you there.
        # After doing all of that, add up the values of dp grid
        # for each point in the column for location finish.
        
        dp = [[0 for j in range(len(locations))] for i in range(fuel + 1)]
        dp[fuel][start] = 1
        
        for i in range(fuel, -1, -1):
            for j in range(len(locations)-1, -1, -1):
                if dp[i][j] == 0:
                    continue
                for st in range(len(locations)):
                    if st != j:
                        if i >= abs(locations[st] - locations[j]):
                            dp[i-abs(locations[st]-locations[j])][st] += dp[i][j]
        total = 0
        for i in range(fuel+1):
            total += dp[i][finish]
        return total % (10**9 + 7)
        
        
        
        '''for i in range(fuel+1):
            dp[i][finish] = 1
        for i in range(1, fuel + 1): # i is amount of fuel
            for j in range(len(locations)): # j is start location
                if i < abs(locations[j] - locations[finish]):
                    dp[i][j] = 0
                elif i == abs(locations[j] - locations[finish]):
                    dp[i][j] = 1
                else:
                    total = 0
                    print(f\"fuel {i} and location {j}\")
                    for st in range(len(locations)):
                        print(f\"next location is {st}\")
                        if abs(locations[st] - locations[j]) >= i:
                            print(\"at 0\")
                            
                            total += dp[i - abs(locations[j] - locations[st])][st]
                            if st == finish:
                                total += 1
                            #print(\"total is now \", total)
                    print(\"final total is \", total)
                    dp[i][j] = total
        print(dp)
        return dp[fuel][start]'''
        
                
        
        '''from functools import lru_cache
        
        @lru_cache
        def dfs(start, fuel):
            #print(\"dfs called with start, fuel: \", start, fuel)
            total = 0
            if start == finish:
                total += 1
            if fuel == 0:
                return total
            for city in range(len(locations)):
                if city != start:
                    if abs(locations[start]-locations[city]) <= fuel:
                        #print(f\"arrived at {city} from {start}\")
                        #if city == finish:
                        #    res[0] += 1
                        newFuel = fuel - abs(locations[start]-locations[city])
                        #print(f\"newFuel is {newFuel}\")
                        if newFuel >= 0: 
                            if city != finish:
                                if fuel >= abs(locations[city]-locations[finish]):
                                    total += dfs(city, newFuel)
                            else:
                                total += dfs(city, newFuel)
            return total
        
        res = dfs(start, fuel)
        return res % (10**9 + 7)'''
        

