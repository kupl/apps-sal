class Solution:
    def helper(self, n, M, curr, piles, memo):
        if curr >= n:
            return 0

        if n - curr <= 2 * M:
            return sum(piles[curr:])

        if (curr, M) in memo:
            return memo[(curr, M)]

        me = 0
        total = sum(piles[curr:])

        for X in range(1, 2 * M + 1):
            opponent = self.helper(n, max(X, M), curr + X, piles, memo)

            me = max(me, total - opponent)

        memo[(curr, M)] = me

        return me

    def stoneGameII(self, piles: List[int]) -> int:
        return self.helper(len(piles), 1, 0, piles, {})
