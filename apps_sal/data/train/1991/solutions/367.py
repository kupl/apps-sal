class Solution:
    d = {}

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        self.loc = sorted(locations)
        self.numloc = len(locations)
        self.num = 10 ** 9 + 7
        Solution.d = {}
        newstart = self.loc.index(locations[start])
        newfinish = self.loc.index(locations[finish])
        ways = self.cr(newstart, newfinish, fuel)
        if newstart == newfinish and ways == 0:
            return 1
        if newstart == newfinish:
            ways += 1
        return ways

    def cr(self, start, finish, fuel):
        if fuel < 0 or fuel < abs(self.loc[finish] - self.loc[start]):
            return 0
        if (start, fuel) in Solution.d:
            return Solution.d[start, fuel]
        minfuel = abs(self.loc[finish] - self.loc[start])
        if fuel <= minfuel + 1:
            Solution.d[start, fuel] = 2 ** (abs(finish - start) - 1)
            return Solution.d[start, fuel]
        ways = 0
        for i in range(self.numloc):
            if i != start:
                fuel1 = abs(self.loc[i] - self.loc[start])
                fuel2 = abs(self.loc[i] - self.loc[finish])
                if fuel1 + fuel2 <= fuel:
                    ways += self.cr(i, finish, fuel - fuel1)
        if start != finish:
            ways += 1
        ways %= self.num
        Solution.d[start, fuel] = ways
        return ways
