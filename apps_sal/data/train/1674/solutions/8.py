class Solution:

    def stoneGameII(self, piles: List[int]) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def select(start, M, my_turn):
            if my_turn:
                if start + 2 * M >= len(piles):
                    return sum(piles[start:])
                rst = 0
                for i in range(1, 2 * M + 1):
                    rst = max(rst, sum(piles[start:start + i]) + select(start + i, max(i, M), False))
                return rst
            if start + 2 * M >= len(piles):
                return 0
            rst = float('inf')
            for i in range(1, 2 * M + 1):
                rst = min(rst, select(start + i, max(i, M), True))
            return rst
        return select(0, 1, True)
