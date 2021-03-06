class Solution:

    def stoneGameII(self, piles: List[int]) -> int:
        self.piles = piles

        @lru_cache(maxsize=None)
        def helper(i, j, M, turn=True):
            if i >= j:
                return 0
            X = list(range(1, 2 * M + 1))
            if turn:
                maxalex = -sys.maxsize
            else:
                maxalex = sys.maxsize
            for x in X:
                if turn:
                    if i + x <= j:
                        alex = sum(self.piles[i:i + x]) + helper(i + x, j, max(x, M), turn=False)
                        maxalex = max(alex, maxalex)
                else:
                    alex = helper(i + x, j, max(x, M), turn=True)
                    maxalex = min(alex, maxalex)
            return maxalex
        return helper(0, len(self.piles), 1)
