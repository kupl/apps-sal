class Solution:
    @lru_cache(1024 * 1024)
    def helper(self, fuel_left, curr, target):
        su = 0
        if curr == target:
            su += 1
        for i in range(len(self.locations)):
            if i == curr:
                continue
            spent = abs(self.locations[curr] - self.locations[i])
            if fuel_left >= spent:
                su += self.helper(fuel_left - spent, i, target)
        return su

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        self.locations = locations
        return self.helper(fuel, start, finish) % (1000000007)
