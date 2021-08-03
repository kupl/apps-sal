class Solution:
    def solve(self, start, end, M, player):
        if (start, end, M, player) in self.dp:
            return self.dp[start, end, M, player]
        maxa = 0
        maxl = 0
        if start > end:
            return [0, 0]

        for i in range(1, 2 * M + 1):
            picked = sum(self.piles[start:start + i])
            if player == 0:
                a, l = self.solve(start + i, end, max(i, M), 1)
                if picked + a > maxa:
                    maxa = picked + a
                    maxl = l
            else:
                a, l = self.solve(start + i, end, max(i, M), 0)
                if picked + l > maxl:
                    maxa = a
                    maxl = picked + l

        self.dp[(start, end, M, player)] = (maxa, maxl)
        return (maxa, maxl)

    def stoneGameII(self, piles: List[int]) -> int:
        self.dp = {}
        self.piles = piles

        ans = self.solve(0, len(piles) - 1, 1, 0)
        print(self.dp)
        return ans[0]
