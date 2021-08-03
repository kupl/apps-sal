from functools import lru_cache


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        self.length = len(locations)
        self.locations = locations
        self.end = finish
        self.mod = 10**9 + 7
        return self.reachEnd(start, fuel) % self.mod

    @lru_cache(None)
    def reachEnd(self, curr, fuel):
        if(fuel < 0):
            return 0
        if(curr == self.end and fuel == 0):
            return 1
        ans = 0
        if(curr == self.end):
            ans += 1
        for index, i in enumerate(self.locations):
            if(curr == index):
                continue
            ans += (self.reachEnd(index, fuel - abs(self.locations[curr] - i))) % self.mod

        return ans % self.mod
