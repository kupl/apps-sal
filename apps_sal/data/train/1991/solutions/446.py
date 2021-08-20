class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        f = [[0] * (fuel + 1) for i in range(n)]
        f[start][fuel] = 1
        for x in range(fuel, 0, -1):
            for i in range(n):
                for j in range(n):
                    t = abs(locations[i] - locations[j])
                    if i != j and t <= x:
                        f[j][x - t] += f[i][x]
        return sum(f[finish]) % (10 ** 9 + 7)
