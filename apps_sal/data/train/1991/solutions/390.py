class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        # print(start, finish, fuel)
        self.mp = {}  # key: start-finish-fuel; val: numWays
        return self.dfs(locations, start, finish, fuel)
    
    def dfs(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        if fuel < 0:
            return 0
        key = '{}-{}-{}'.format(start, finish, fuel)
        if key in self.mp:
            return self.mp[key]
        res = 1 if start == finish else 0
        for i in range(len(locations)):
            if i != start:
                res += self.dfs(locations, i, finish, fuel-abs(locations[start]-locations[i]))
        res %= (10**9 + 7)
        self.mp[key] = res
        return res

