import functools
import sys


class Solution:

    @lru_cache(None)
    def rec(self, i, fuel):
        if fuel == 0 and i != self.finish:
            return 0
        if i == self.finish and fuel == 0:
            return 1
        if i == self.finish:
            ans = 1
        else:
            ans = 0
        for j in range(len(self.locations)):
            diff = abs(self.locations[j] - self.locations[i])
            if i != j and diff <= fuel:
                ans += self.rec(j, fuel - diff)
                ans %= self.MOD
        return ans

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        self.MOD = 10 ** 9 + 7
        self.locations = locations
        self.finish = finish
        sys.setrecursionlimit(1500)
        return self.rec(start, fuel)
