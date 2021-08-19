class Solution:

    @functools.lru_cache(None)
    def core(self, start, finish, fuel):
        if fuel < 0:
            return 0
        elif abs(self.locs[start] - self.locs[finish]) > fuel:
            return 0
        elif fuel == 0:
            return 1 if start == finish else 0
        else:
            i = start - 1
            cntr = 1 if start == finish else 0
            while i >= 0:
                cost = self.locs[start] - self.locs[i]
                if 2 * cost > fuel and finish >= start or cost > fuel:
                    break
                cntr += self.core(i, finish, fuel - cost)
                cntr %= self.mod
                i -= 1
                pass
            i = start + 1
            while i < len(self.locs):
                cost = self.locs[i] - self.locs[start]
                if 2 * cost > fuel and finish <= start or cost > fuel:
                    break
                cntr += self.core(i, finish, fuel - cost)
                cntr %= self.mod
                i += 1
                pass
            return cntr
        pass

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        self.mod = 1000000007
        self.locs = locations
        s = locations[start]
        d = locations[finish]
        self.locs.sort()
        start = self.locs.index(s)
        finish = self.locs.index(d)
        return self.core(start, finish, fuel)
