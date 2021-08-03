class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        locLen = len(locations)
        MOD = 10**9 + 7
        dp = {}

        def helper(i, f):
            if (i, f) in dp:
                return dp[(i, f)]
            subAns = 0
            for i1 in range(locLen):
                if i1 == i or abs(locations[i1] - locations[i]) > f:
                    continue
                if i1 == finish:
                    subAns += (1 + helper(i1, f - abs(locations[i1] - locations[i])))
                else:
                    subAns += helper(i1, f - abs(locations[i1] - locations[i]))
            dp[(i, f)] = subAns % MOD
            return dp[(i, f)]

        return helper(start, fuel) + (1 if start == finish else 0)
