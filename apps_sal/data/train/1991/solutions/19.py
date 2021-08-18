class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        f = [[0 for j in range(n)] for i in range(fuel + 1)]
        LARGE = int(1e9 + 7)
        f[fuel][start] = 1
        for v in range(fuel, -1, -1):
            for i, loc1 in enumerate(locations):
                if (f[v][i] > 0):
                    for j, loc2 in enumerate(locations):
                        if (j != i):
                            update_fuel = v - abs(loc1 - loc2)
                            if (update_fuel >= 0):
                                f[update_fuel][j] += f[v][i] % LARGE
        result = sum([f[i][finish] for i in range(fuel)])
        if (start == finish):
            result += 1
        return result % LARGE
