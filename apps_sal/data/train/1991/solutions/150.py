class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = {}
        
        def recursive(curr, fuel):
            count = 0

            if (curr, fuel) in dp:
                return dp[curr, fuel]
            
            elif curr == finish:
                count += 1
            
            for c in range(len(locations)):
                fuelRequired = abs(locations[c] - locations[curr])
                
                if c != curr and fuel >= fuelRequired:
                    count += recursive(c, fuel - fuelRequired)

            dp[curr, fuel] = count % 1000000007
            
            return dp[curr, fuel]
        
        return recursive(start, fuel)
