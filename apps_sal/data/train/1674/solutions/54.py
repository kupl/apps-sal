class Solution:

    def stoneGameII(self, piles: List[int]) -> int:

        @lru_cache(maxsize=None)
        def minmax(st, m, player):
            if st >= len(piles):
                return 0
            if player:
                return max([sum(piles[st:st + x]) + minmax(st + x, max(x, m), player ^ 1) for x in range(1, 2 * m + 1)])
            else:
                return min([minmax(st + x, max(m, x), player ^ 1) for x in range(1, 2 * m + 1)])
        return minmax(0, 1, 1)
