class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = {}
        
        def recursive(curr, fuel):
            key = (curr, fuel)
            count = 0

            if curr == finish:
                count += 1
            
            elif key in dp:
                return dp[key]
            
            for c in range(len(locations)):
                fuelRequired = abs(locations[c] - locations[curr])
                
                if c != curr and fuel >= fuelRequired:
                    count += recursive(c, fuel - fuelRequired)

            dp[key] = count
            
            return dp[key]
        
        return recursive(start, fuel) % (10**9 + 7)
