class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        memo = [[-1]*(fuel+1) for i in range(n)]
        mod = 10**9 + 7
        def dp(curr, fuel):
            if fuel < 0:
                return 0
            
            if memo[curr][fuel] != -1:
                return memo[curr][fuel]
            
            memo[curr][fuel] = 1 if curr == finish else 0
            
            for i, city in enumerate(locations):
                if i != curr:
                    memo[curr][fuel] += dp(i, fuel - abs(city - locations[curr]))
                    memo[curr][fuel] %= mod

            return memo[curr][fuel]
        
        return dp(start,fuel)
