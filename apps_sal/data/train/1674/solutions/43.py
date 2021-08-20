class Solution:

    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        prefix_sum = [0] * (n + 1)
        for i in range(1, len(prefix_sum)):
            prefix_sum[i] = prefix_sum[i - 1] + piles[i - 1]
        memo = {}

        def dfs(pos, m, player1):
            if pos >= len(piles):
                return (0, 0)
            if (pos, m, int(player1)) in memo:
                return memo[pos, m, int(player1)]
            if player1:
                best_score = -sys.maxsize
                p1_score = 0
            else:
                best_score = sys.maxsize
                p1_score = 0
            for x in range(1, 2 * m + 1):
                if pos + x > len(piles):
                    break
                (score, p1_score_candidate) = dfs(pos + x, max(m, x), not player1)
                if player1:
                    score += prefix_sum[pos + x] - prefix_sum[pos]
                    if score > best_score:
                        p1_score = p1_score_candidate + prefix_sum[pos + x] - prefix_sum[pos]
                        best_score = score
                else:
                    score += -prefix_sum[pos + x] + prefix_sum[pos]
                    if score < best_score:
                        best_score = score
                        p1_score = p1_score_candidate
            memo[pos, m, int(player1)] = (best_score, p1_score)
            return (best_score, p1_score)
        return dfs(0, 1, True)[1]
