class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)
        self.dp = {}

        def recursiveStoneGame(start, M):
            if start >= N:
                return 0

            if start == N - 1:
                return piles[start]

            if (start, M) in self.dp:
                return self.dp[(start, M)]

            alex = 0
            for x in range(1, 2 * M + 1):
                opponent_score = recursiveStoneGame(start + x, max(x, M))
                this_score = sum(piles[start:]) - opponent_score

                alex = max(alex, this_score)

            self.dp[(start, M)] = alex

            return alex

        result = recursiveStoneGame(0, 1)
        return result
