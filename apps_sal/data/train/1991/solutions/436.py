# (city,loc)
# [(0,2),(1,3),(2,6),(3,8),(4,4)]
# 012345678
# ..014.2.3
# p[x,f] = sum (p[i,f + dist(i,x)] if i!=x and dist(i,x) <= f)
# trivial case
# p[start,fuel] = 1
# p[x,fuel] = 0 if x != start
# p[x,fuel-1] = ..
# return p[finish,0]

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

        # print(grid)
        return sum(grid[finish]) % (pow(10, 9) + 7)
