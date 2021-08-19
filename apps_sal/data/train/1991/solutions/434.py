class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        bk = [[0 for _ in range(len(locations))] for __ in range(fuel + 1)]
        bk[-1][start] = 1
        for f in range(fuel, -1, -1):
            for (i, at) in enumerate(locations):
                for (j, to) in enumerate(locations):
                    if i == j:
                        continue
                    need = abs(at - to)
                    if f >= need:
                        bk[f - need][j] += bk[f][i]
        mod = 10 ** 9 + 7
        return sum((bk[i][finish] for i in range(fuel + 1))) % mod
