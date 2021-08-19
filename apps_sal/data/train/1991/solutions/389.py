class Solution:
    mps = []

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        self.mps = []
        for i in range(len(locations)):
            self.mps.append({})
        return self.dfs(locations, start, finish, fuel) % (10 ** 9 + 7)

    def dfs(self, locations, cur, finish, fuel):
        if fuel in self.mps[cur]:
            return self.mps[cur][fuel]
        ans = 0
        if cur == finish:
            ans += 1
        if fuel == 0:
            return ans
        for i in range(len(locations)):
            if i != cur:
                cost = abs(locations[i] - locations[cur])
                if cost <= fuel:
                    ans += self.dfs(locations, i, finish, fuel - cost)
        self.mps[cur][fuel] = ans
        return ans
