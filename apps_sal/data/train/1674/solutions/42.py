class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @lru_cache(None)
        def minimax(start, m, player):
            if start >= len(piles):
                return 0
            if player == 1:
                return max(sum(piles[start:start + x]) + minimax(start + x, max(x, m), 2) for x in range(1, 2 * m + 1))
            if player == 2:
                return min(minimax(start + x, max(x, m), 1) for x in range(1, 2 * m + 1))
        return minimax(0, 1, 1)
