class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = {}

        def recursive(curr, finish, fuel):
            key = (curr, fuel)
            count = 0
            if fuel < 0:
                return 0

            elif curr == finish:
                count += 1

            elif key in dp:
                return dp[key]

            count += sum([recursive(c, finish, fuel - abs(locations[c] - locations[curr])) for c in range(len(locations)) if c != curr])
            dp[key] = count

            return dp[key]

        return recursive(start, finish, fuel) % (10**9 + 7)
