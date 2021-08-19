class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dic = {}
        for (i, l) in enumerate(locations):
            dic[l] = i
        idxes = sorted(dic.keys())
        MOD = 10 ** 9 + 7
        from functools import lru_cache

        @lru_cache(None)
        def dp(i, k):
            if i == finish:
                res = 1
            else:
                res = 0
            L = bisect.bisect_left(idxes, locations[i] - k)
            R = bisect.bisect_right(idxes, locations[i] + k)
            if L == R == i:
                return res
            for j in range(L, R):
                if dic[idxes[j]] != i:
                    res += dp(dic[idxes[j]], k - abs(locations[i] - idxes[j])) % MOD
            return res
        return dp(start, fuel) % MOD
