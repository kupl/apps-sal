class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        
        memo = {}
        
        def dp(ind, rem_fuel):
            if (ind, rem_fuel) in memo:
                return memo[(ind, rem_fuel)]
            num_ways = 0
            for city in range(len(locations)):
                used = abs(locations[ind] - locations[city])
                if used <= rem_fuel and city != ind:
                    num_ways += dp(city, rem_fuel-used)
                    if city == finish:
                        num_ways += 1
            memo[(ind, rem_fuel)] = num_ways
            return memo[(ind, rem_fuel)]
        
        res = dp(start, fuel)
        if start == finish:
            res += 1
        return res%(10**9+7)
