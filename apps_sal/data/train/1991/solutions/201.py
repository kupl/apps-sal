MOD = int(1e9 + 7)


class Solution:
    def num_routes(self, start, finish, fuel):
        min_fuel = abs(self.loc[start] - self.loc[finish])
        if fuel < min_fuel:
            return 0
        if fuel == 0:
            return 1 if start == finish else 0

        try:
            return self.cache[(start, finish, fuel)]
        except KeyError:
            ret = 1 if start == finish else 0
            for first_stop in range(len(self.loc)):
                if first_stop == start:
                    continue
                first_fuel = abs(self.loc[start] - self.loc[first_stop])
                if fuel < first_fuel:
                    continue
                ret = (ret + self.num_routes(first_stop, finish, fuel - first_fuel)) % MOD
            self.cache[(start, finish, fuel)] = ret
            return ret

    def countRoutes(self, locations, start, finish, fuel):
        self.loc = locations
        self.cache = {}
        return self.num_routes(start, finish, fuel)
