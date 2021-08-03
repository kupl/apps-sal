class Solution:
    @lru_cache(1024 * 1024)
    def helper(self, fuel_left, curr, target):
        su = 0
        # if fuel_left < 0:
        #     return 0
        if curr == target:
            su += 1
        for i in range(len(self.locations)):
            if i == curr:
                continue
            spent = abs(self.locations[curr] - self.locations[i])
            if fuel_left >= spent:
                su += self.helper(fuel_left - spent, i, target)
        # print('fuel_left =', fuel_left)
        # print('here =', self.locations[curr])
        # print('ans =', su)
        return su

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        self.locations = locations
        # self.street = sorted(locations)
        # self.count = 0
        return self.helper(fuel, start, finish) % (1000000007)
