class Solution:

    def stoneGameII(self, a: List[int]) -> int:

        @lru_cache(maxsize=None)
        def minimax(start, m, alex):
            if start >= len(a):
                return 0
            if alex:
                return max([sum(a[start:start + x]) + minimax(start + x, max(m, x), not alex) for x in range(1, 2 * m + 1)])
            else:
                return min([minimax(start + x, max(m, x), not alex) for x in range(1, 2 * m + 1)])
        return minimax(0, 1, True)
