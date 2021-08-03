from functools import lru_cache


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        start = locations[start]
        finish = locations[finish]

        @lru_cache(None)
        def helper(start, fuel):
            if fuel < 0:
                return 0
            summ = start == self.finish
            for i in locations:
                if i != start:
                    remaining_fuel = fuel - abs(start - i)
                    summ += helper(i, remaining_fuel)
            print((start, fuel, summ))
            return summ
        self.finish = finish
        return helper(start, fuel) % (10**9 + 7)
