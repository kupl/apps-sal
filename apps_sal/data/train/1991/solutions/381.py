from functools import lru_cache


class Solution:
    @lru_cache(None)
    def solve(self, curr, fuel):
        if fuel < 0:
            return 0
        if fuel == 0 and curr != self.fin:
            return 0
        ans = 0
        if curr == self.fin:
            ans += 1
        for i in range(len(self.loc)):
            if i == curr:
                continue
            ans += self.solve(i, fuel - abs(self.loc[i] - self.loc[curr]))
            ans %= self.mod
        return ans

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        self.mod = 1000000007
        self.loc = locations
        self.fin = finish
        return self.solve(start, fuel) % self.mod
