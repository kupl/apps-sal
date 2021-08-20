class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        (n, m) = (len(locations), 1000000007)
        s = [[0] * n for _ in range(fuel + 1)]
        s[fuel][start] = 1
        for i in range(fuel, 0, -1):
            for j in range(n):
                for k in range(j):
                    t = abs(locations[j] - locations[k])
                    if t <= i:
                        s[i - t][k] = (s[i - t][k] + s[i][j]) % m
                for k in range(j + 1, n):
                    t = abs(locations[j] - locations[k])
                    if t <= i:
                        s[i - t][k] = (s[i - t][k] + s[i][j]) % m
        return sum([s[i][finish] for i in range(fuel + 1)]) % m
