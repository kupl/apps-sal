class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        DP = [[-1] * len(locations) for _ in range(fuel + 1)]

        ans = self.dfs(locations, start, finish, fuel, DP, start) % (10**9 + 7)

        return ans

    def dfs(self, locations, start, finish, fuel, DP, cur):
        paths = 0
        if cur == finish and fuel >= 0:
            paths += 1

        for i in range(len(locations)):
            if i == cur:
                continue

            if fuel - abs(locations[i] - locations[cur]) < 0:
                continue

            if DP[fuel - abs(locations[i] - locations[cur])][i] == -1:
                DP[fuel - abs(locations[i] - locations[cur])][i] = self.dfs(locations, start, finish,
                                                                            fuel - abs(locations[i] - locations[cur]),
                                                                            DP, i)
            paths += DP[fuel - abs(locations[i] - locations[cur])][i]

        return paths
