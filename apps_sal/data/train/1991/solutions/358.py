class Solution:
    # dp(loc, fuel) = sum(dp(pre_loc, fuel + abs(loc-pre_loc)))
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        M = 10**9 + 7

        @lru_cache(None)
        def dp(curLocation, curFuel):
            if curFuel > fuel:
                return 0
            nonlocal M
            count = 0
            for preLocation in locations:
                if preLocation == curLocation:
                    continue
                preFuel = curFuel + abs(preLocation - curLocation)
                if preFuel > fuel or (preFuel == fuel and preLocation != locations[start]):
                    continue
                if preLocation == locations[start] and preFuel == fuel:
                    count = (count + 1) % M
                else:
                    count = (count + dp(preLocation, preFuel)) % M
            return count % M

        ans = sum([dp(locations[finish], f) % M for f in range(fuel)]) % M
        return ans + 1 if start == finish else ans
