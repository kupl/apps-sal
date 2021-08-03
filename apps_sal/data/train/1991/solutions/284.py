class Solution:
    # 1575
    def countRoutes(self, locations: 'List[int]', start: int, finish: int, fuel: int) -> int:
        MOD = 1000000007
        sp, ep = locations[start], locations[finish]
        locations.sort()
        s, e = locations.index(sp), locations.index(ep)
        N = len(locations)

        @functools.lru_cache(None)
        def helper(i, f):
            if i != e and abs(locations[e] - locations[i]) <= f:
                res = 1
            else:
                res = 0
            j = i - 1
            while j >= 0 and abs(locations[i] - locations[j]) + abs(locations[e] - locations[j]) <= f:
                res += helper(j, f - abs(locations[i] - locations[j]))
                j -= 1
            j = i + 1
            while j < N and abs(locations[i] - locations[j]) + abs(locations[e] - locations[j]) <= f:
                res += helper(j, f - abs(locations[j] - locations[i]))
                j += 1
            return res % MOD
        return helper(s, fuel) + (s == e)
