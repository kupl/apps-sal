class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        self.memo = {}
        return self.dfs(start, fuel, finish, locations) % (10 ** 9 + 7)

    def dfs(self, location, fuel, finish, locations):
        if (location, fuel) in self.memo:
            return self.memo[location, fuel]
        if fuel < 0:
            return 0
        ways = 0 if location != finish else 1
        for i in range(len(locations)):
            if i == location:
                continue
            ways += self.dfs(i, fuel - abs(locations[i] - locations[location]), finish, locations)
        self.memo[location, fuel] = ways
        return ways
