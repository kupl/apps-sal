class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        dp = [[0 for j in range(len(locations))] for i in range(fuel + 1)]
        dp[fuel][start] = 1

        for i in range(fuel, -1, -1):
            for j in range(len(locations) - 1, -1, -1):
                if dp[i][j] == 0:
                    continue
                for st in range(len(locations)):
                    if st != j:
                        if i >= abs(locations[st] - locations[j]):
                            dp[i - abs(locations[st] - locations[j])][st] += dp[i][j]
        total = 0
        for i in range(fuel + 1):
            total += dp[i][finish]
        return total % (10**9 + 7)

        '''for i in range(fuel+1):
            dp[i][finish] = 1
        for i in range(1, fuel + 1): 
            for j in range(len(locations)): 
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
                    print(\"final total is \", total)
                    dp[i][j] = total
        print(dp)
        return dp[fuel][start]'''

        '''from functools import lru_cache
        
        @lru_cache
        def dfs(start, fuel):
            total = 0
            if start == finish:
                total += 1
            if fuel == 0:
                return total
            for city in range(len(locations)):
                if city != start:
                    if abs(locations[start]-locations[city]) <= fuel:
                        newFuel = fuel - abs(locations[start]-locations[city])
                        if newFuel >= 0: 
                            if city != finish:
                                if fuel >= abs(locations[city]-locations[finish]):
                                    total += dfs(city, newFuel)
                            else:
                                total += dfs(city, newFuel)
            return total
        
        res = dfs(start, fuel)
        return res % (10**9 + 7)'''
