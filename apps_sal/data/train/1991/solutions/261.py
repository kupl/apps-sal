class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        memo = {}

        def helper(fuell, curr):
            if (fuell, curr) in memo:
                return memo[fuell, curr]
            if fuell < 0:
                return 0
            x = 0
            if curr == locations[finish]:
                x = 1
            y = x + sum([helper(fuell - abs(loc - curr), loc) for loc in locations if loc != curr]) % (10 ** 9 + 7)
            memo[fuell, curr] = y
            return y
        return helper(fuel, locations[start])
