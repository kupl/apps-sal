class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        @lru_cache(None)
        def helper(startInd, remainFuel):
            if remainFuel < 0:
                return 0
            if abs(locations[finish] - locations[startInd]) > remainFuel:
                return 0
            if remainFuel == 0:
                return 1

            res = 1 if startInd == finish else 0
            for i in range(0, len(locations)):
                if i == startInd or abs(locations[i] - locations[startInd]) > remainFuel:
                    continue
                res += helper(i, remainFuel - abs(locations[i] - locations[startInd]))
            return res % (10**9 + 7)

        return helper(start, fuel)
