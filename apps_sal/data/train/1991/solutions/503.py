class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        N = len(locations)
        self.dp = {(start, fuel): 1}
        res = 0
        for f in range(fuel, -1, -1):
            for u in range(N):
                if (u, f) not in self.dp:
                    continue
                ways = self.dp[u, f]
                for v in range(N):
                    dist = abs(locations[u] - locations[v])
                    if u == v or dist > f:
                        continue
                    if (v, f - dist) not in self.dp:
                        self.dp[v, f - dist] = 0
                    self.dp[v, f - dist] = (self.dp[v, f - dist] + self.dp[u, f]) % (int(1000000000.0) + 7)
            if (finish, f) in self.dp:
                res = (res + self.dp[finish, f]) % (int(1000000000.0) + 7)
        return res
