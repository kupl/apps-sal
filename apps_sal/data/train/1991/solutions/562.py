class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 1000000007

        @functools.lru_cache(maxsize=None)
        def calc(start, fuel):
            ret = 0
            if start == finish:
                ret += 1
            for i in range(len(locations)):
                if i == start:
                    continue
                d = abs(locations[i] - locations[start])
                if d > fuel:
                    continue
                ret = (ret + calc(i, fuel - d)) % MOD
            return ret

        return calc(start, fuel)
