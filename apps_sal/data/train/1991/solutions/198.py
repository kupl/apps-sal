class Solution:

    def search(self, locations, start, finish, fuel):
        if (start, fuel) in self.memo:
            return self.memo[start, fuel]
        count = 0
        if start == finish:
            count += 1
        for (i, loc) in enumerate(locations):
            dist = abs(locations[start] - loc)
            if i == start or dist > fuel:
                continue
            count += self.search(locations, i, finish, fuel - dist)
        self.memo[start, fuel] = count % (10 ** 9 + 7)
        return self.memo[start, fuel]

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        self.memo = {}
        return self.search(locations, start, finish, fuel)
