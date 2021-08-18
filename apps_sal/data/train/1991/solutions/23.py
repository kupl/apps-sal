from functools import lru_cache


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        start_pos = locations[start]
        end_pos = locations[finish]
        N = len(locations)

        @lru_cache(None)
        def route(x, f):

            if abs(end_pos - x) > f:
                return 0

            if end_pos == x:
                ans = 1
            else:
                ans = 0

            for y in locations:
                if x != y:
                    ans += route(y, f - abs(x - y))

            return ans

        return route(start_pos, fuel) % (10**9 + 7)
