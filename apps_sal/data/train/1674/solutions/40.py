class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        prefix_sum = [0] * (n + 1)
        for i in range(1, len(prefix_sum)):
            prefix_sum[i] = prefix_sum[i - 1] + piles[i - 1]
        memo = {}

        def dfs(pos, m, player1):
            if pos >= len(piles):
                return 0
            if (pos, m, int(player1)) in memo:
                return memo[(pos, m, int(player1))]

            if player1:
                best_score = -sys.maxsize
            else:
                best_score = sys.maxsize

            for x in range(1, 2 * m + 1):
                if pos + x > len(piles):
                    break
                score = dfs(pos + x, max(m, x), not player1)
                if player1:
                    score += prefix_sum[pos + x] - prefix_sum[pos]
                    best_score = max(best_score, score)
                else:
                    best_score = min(best_score, score)
            memo[(pos, m, int(player1))] = best_score
            return best_score
        return dfs(0, 1, True)
