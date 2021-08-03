from functools import lru_cache


class Solution:

    @lru_cache(None)
    def dp(self, start, fuel):
        r = 0
        if fuel < 0:
            return 0
        if start == self.finish:
            r += 1
        for l in self.locations:
            if start == l:
                continue
            r += self.dp(l, fuel - abs(start - l))
        #print(start, fuel, r, self.finish)
        return r

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        # print(\"===\")
        self.finish = locations[finish]
        self.locations = locations
        return self.dp(locations[start], fuel) % (10**9 + 7)
