class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)

        @lru_cache(None)
        def helper(ind, f):
            ret = 0
            if ind == finish:
                ret += 1
            for i in range(n):
                if i != ind and abs(locations[i] - locations[ind]) <= f:
                    ret += helper(i, f - abs(locations[i] - locations[ind]))
            return ret
        return helper(start, fuel) % (10**9 + 7)
