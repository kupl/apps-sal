class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        M = len(locations)
        dp = [M * [0] for _ in range(fuel + 1)]
        dp[0][start] = 1
        dis = dict()
        for i in range(M):
            dis[(i, i)] = float('inf')
            for j in range(M):
                if i != j:
                    dis[(i, j)] = abs(locations[i] - locations[j])
        Z = 10**9 + 7
        for i in range(1, fuel + 1):
            for j in range(M):
                for k in range(M):
                    if dis[(k, j)] <= i:
                        dp[i][j] += dp[i - dis[(k, j)]][k]
                dp[i][j] %= Z
        total = sum(dp[i][finish] for i in range(1, fuel + 1)) % Z
        if finish == start:
            return total + 1
        else:
            return total
