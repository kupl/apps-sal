class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 10 ** 9 + 7

        @functools.lru_cache(None)
        def drive(i, fuel):
            res = 0
            if i == finish:
                res += 1
            for j in range(len(locations)):
                if i == j:
                    continue
                dist = abs(locations[i] - locations[j])
                if dist <= fuel:
                    res += drive(j, fuel - dist) % mod
            return res % mod
        return drive(start, fuel)
