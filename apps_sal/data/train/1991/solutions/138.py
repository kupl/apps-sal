class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = {}

        def recursive(curr, fuel):

            if (curr, fuel) in dp:
                return dp[curr, fuel]

            count = 1 if curr == finish else 0

            for c in range(len(locations)):
                fuelRequired = abs(locations[c] - locations[curr])

                if c != curr and fuel >= fuelRequired:
                    count += recursive(c, fuel - fuelRequired)

            dp[curr, fuel] = count % (10**9 + 7)

            return dp[curr, fuel]

        return recursive(start, fuel)
