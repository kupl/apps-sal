class Solution:
    def countRoutes(self, locations: [int], start: int, finish: int, fuel: int) -> int:
        d = {}

        start = locations[start]
        finish = locations[finish]
        for x in locations:
            d[x] = [0] * 201
        d[start][fuel] = 1
        ans = 0
        for fu in range(200, 0, -1):
            for loc in d:
                if d[loc][fu] != 0:
                    for x in d:
                        if x == loc:
                            continue
                        result = fu - abs(x - loc)
                        if result >= 0:
                            d[x][result] += d[loc][fu]
                            d[x][result] %= 10**9 + 7

        return sum(d[finish]) % (10**9 + 7)


print(Solution().countRoutes([2, 3, 6, 8, 4], 1, 3, 5))
