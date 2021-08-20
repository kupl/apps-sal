class Solution:
    mod = 10 ** 9 + 7

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        self.res = 0
        self.locations = locations
        return self.traverse(start, finish, fuel)

    @lru_cache(None)
    def traverse(self, current, finish, fuel):
        if fuel < 0:
            return 0
        res = 1 if current == finish else 0
        for i in range(len(self.locations)):
            if i == current:
                continue
            res += self.traverse(i, finish, fuel - abs(self.locations[i] - self.locations[current]))
        return res % self.mod
