class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        self.locations = locations
        self.cache = [{} for i in range(len(locations))]
        re = self.dfs(start, finish, fuel)
        return re % (pow(10, 9) + 7)

    def dfs(self, start, tmpend, fu):
        if fu in list(self.cache[tmpend].keys()):
            return self.cache[tmpend][fu]
        if fu < 0:
            return 0
        if fu == 0:
            self.cache[tmpend][0] = 0 if start != tmpend else 1
            return self.cache[tmpend][0]
        self.cache[tmpend][fu] = 0
        for i in range(len(self.locations)):
            if i == tmpend:
                continue
            self.cache[tmpend][fu] += self.dfs(start, i, fu - abs(self.locations[i] - self.locations[tmpend]))
        if start == tmpend:
            self.cache[tmpend][fu] += 1
        return self.cache[tmpend][fu]
