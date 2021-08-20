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
        return total % (10 ** 9 + 7)
        'for i in range(fuel+1):\n            dp[i][finish] = 1\n        for i in range(1, fuel + 1): # i is amount of fuel\n            for j in range(len(locations)): # j is start location\n                if i < abs(locations[j] - locations[finish]):\n                    dp[i][j] = 0\n                elif i == abs(locations[j] - locations[finish]):\n                    dp[i][j] = 1\n                else:\n                    total = 0\n                    print(f"fuel {i} and location {j}")\n                    for st in range(len(locations)):\n                        print(f"next location is {st}")\n                        if abs(locations[st] - locations[j]) >= i:\n                            print("at 0")\n                            \n                            total += dp[i - abs(locations[j] - locations[st])][st]\n                            if st == finish:\n                                total += 1\n                            #print("total is now ", total)\n                    print("final total is ", total)\n                    dp[i][j] = total\n        print(dp)\n        return dp[fuel][start]'
        'from functools import lru_cache\n        \n        @lru_cache\n        def dfs(start, fuel):\n            #print("dfs called with start, fuel: ", start, fuel)\n            total = 0\n            if start == finish:\n                total += 1\n            if fuel == 0:\n                return total\n            for city in range(len(locations)):\n                if city != start:\n                    if abs(locations[start]-locations[city]) <= fuel:\n                        #print(f"arrived at {city} from {start}")\n                        #if city == finish:\n                        #    res[0] += 1\n                        newFuel = fuel - abs(locations[start]-locations[city])\n                        #print(f"newFuel is {newFuel}")\n                        if newFuel >= 0: \n                            if city != finish:\n                                if fuel >= abs(locations[city]-locations[finish]):\n                                    total += dfs(city, newFuel)\n                            else:\n                                total += dfs(city, newFuel)\n            return total\n        \n        res = dfs(start, fuel)\n        return res % (10**9 + 7)'
