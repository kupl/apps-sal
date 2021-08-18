
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        grid = [[0] * (fuel + 1) for _ in range(len(locations))]

        grid[start][fuel] = 1

        for f in range(fuel - 1, -1, -1):
            for i in range(len(locations)):
                s = 0
                for k in range(len(locations)):
                    dist = abs(locations[i] - locations[k])
                    if i != k and f + dist <= fuel:
                        s += grid[k][f + dist]
                grid[i][f] = s

        return sum(grid[finish]) % (pow(10, 9) + 7)
