class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n, mod = len(locations), 10 ** 9 + 7
        save = [[0] * (fuel + 1) for i in range(n)]
        save[start][fuel] = 1
        for f in range(fuel, 0, -1):
            for i in range(n):
                for j in range(n):
                    if i != j:
                        cur = f - abs(locations[i] - locations[j])
                        if cur >= 0:
                            save[j][cur] = (save[j][cur] + save[i][f]) % mod
        return sum(save[finish]) % mod
