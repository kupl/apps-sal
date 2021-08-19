class Solution:

    def countRoutes(self, loc: List[int], start: int, finish: int, fuel: int) -> int:

        @lru_cache(None)
        def get(cur, left):
            if left < 0:
                return 0
            res = 0
            if cur == finish:
                res += 1
            for i in range(len(loc)):
                if i == cur:
                    continue
                res += get(i, left - abs(loc[i] - loc[cur]))
                res %= 1000000007
            return res
        return get(start, fuel)
