class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        sloc = sorted([(x, i) for i, x in enumerate(locations)])
        froutes = [[0] * n for _ in range(fuel + 1)]
        st, fn = -1, -1
        for i in range(n):
            if sloc[i][1] == start:
                st = i
            if sloc[i][1] == finish:
                fn = i
        froutes[fuel][st] = 1
        f0 = fuel
        while fuel > 0:
            for i, cnt in enumerate(froutes[fuel]):
                if cnt > 0:
                    for j in range(i - 1, -1, -1):
                        dist = sloc[i][0] - sloc[j][0]
                        if dist <= fuel:
                            froutes[fuel - dist][j] += cnt
                        else:
                            break
                    for j in range(i + 1, n):
                        dist = sloc[j][0] - sloc[i][0]
                        if dist <= fuel:
                            froutes[fuel - dist][j] += cnt
                        else:
                            break
            fuel -= 1
        res = 0
        for i in range(f0 + 1):
            res += froutes[i][fn]
        return res % (10**9 + 7)
