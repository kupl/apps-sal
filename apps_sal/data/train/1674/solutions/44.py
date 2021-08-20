class Solution:

    def stoneGameII(self, piles: List[int]) -> int:
        length = len(piles)
        dp = [[0] * length for i in range(length)]
        visited = [[0] * (length + 1) for i in range(length + 1)]

        def helper(index, M):
            if index == length:
                return 0
            if visited[index][M] != 0:
                return dp[index][M]
            best = float('-inf')
            for i in range(1, 2 * M + 1):
                astones = sum(piles[index:index + i])
                score = astones - helper(min(index + i, length), min(max(M, i), length))
                best = max(score, best)
            dp[index][M] = best
            visited[index][M] = 1
            return best
        total = sum(piles)
        diff = helper(0, 1)
        return (total + diff) // 2
