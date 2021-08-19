from functools import lru_cache


class Solution:

    @lru_cache(None)
    def recursive(self, i, f):
        ans = 0
        if i == self.t:
            ans += 1
        if f > 0:
            j = i + 1
            while j < self.n and self.L[j] - self.L[i] + self.m[j] <= f:
                ans += self.recursive(j, f - (self.L[j] - self.L[i]))
                j += 1
            j = i - 1
            while j > -1 and self.L[i] - self.L[j] + self.m[j] <= f:
                ans += self.recursive(j, f - (self.L[i] - self.L[j]))
                j -= 1
        return ans

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        self.n = len(locations)
        (sx, tx) = (locations[start], locations[finish])
        self.L = sorted(locations)
        self.d = {x: i for (i, x) in enumerate(self.L)}
        (self.s, self.t) = (self.d[sx], self.d[tx])
        self.m = {i: abs(x - tx) for (i, x) in enumerate(self.L)}
        self.recursive.cache_clear()
        return self.recursive(self.s, fuel) % (10 ** 9 + 7)
