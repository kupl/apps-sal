class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        M = 10**9 + 7

        @lru_cache(None)
        def dp(locId, curFuel):
            if curFuel > fuel:
                return 0
            nonlocal M
            count = 0
            curLocation = locations[locId]
            for i in range(len(locations)):
                if i == locId:
                    continue
                preLocation = locations[i]
                preFuel = curFuel + abs(preLocation - curLocation)
                if preLocation == locations[start] and preFuel == fuel:
                    count = (count + 1) % M
                if preFuel >= fuel:
                    continue
                count = (count + dp(i, preFuel)) % M
            return count % M

        ans = sum([dp(finish, f) % M for f in range(fuel)]) % M
        return ans + 1 if start == finish else ans
