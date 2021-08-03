class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        x = locations[start]
        y = locations[finish]
        locations.sort()
        u = bisect.bisect_left(locations, x)
        v = bisect.bisect_left(locations, y)

        MOD = int(1e9) + 7

        @lru_cache(None)
        def f(x, left):
            lb = bisect.bisect_left(locations, locations[x] - left)
            rb = bisect.bisect_right(locations, locations[x] + left)

            ret = int(x == v)
            for i in range(lb, rb):
                if i != x:
                    ret += f(i, left - abs(locations[i] - locations[x]))
                    ret %= MOD
            return ret

        return f(u, fuel)
