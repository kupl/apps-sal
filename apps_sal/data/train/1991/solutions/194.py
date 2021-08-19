class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        def helper(curr, fuelLeft, memo, locations, finish, mod):
            if (curr, fuelLeft) in memo:
                return memo[curr, fuelLeft]
            ret = 0
            if curr == finish:
                ret += 1
            for (i, loc) in enumerate(locations):
                if curr != i:
                    candidFuel = fuelLeft - abs(locations[curr] - loc)
                    if candidFuel > 0:
                        ret = (ret + helper(i, candidFuel, memo, locations, finish, mod)) % mod
                    elif candidFuel == 0 and i == finish:
                        ret += 1
            memo[curr, fuelLeft] = ret % mod
            return ret
        return helper(start, fuel, {}, locations, finish, 10 ** 9 + 7)
