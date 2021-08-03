class Solution:
    def rec(self, i, m, t):
        if self.memo[i][m][t] != -1:
            return self.memo[i][m][t]

        if i == self.n:
            return 0

        if t == 0:
            res, now = 0, 0

            for j in range(2 * m):
                if i + j >= self.n:
                    break
                now += self.piles[i + j]
                res = max(res, now + self.rec(i + j + 1, max(m, j + 1), 1))
        else:
            res = 10**18

            for j in range(2 * m):
                if i + j >= self.n:
                    break
                res = min(res, self.rec(i + j + 1, max(m, j + 1), 0))

        self.memo[i][m][t] = res
        return res

    def stoneGameII(self, piles: List[int]) -> int:
        self.n = len(piles)
        self.piles = piles
        self.memo = [[[-1] * 2 for _ in range(110)] for _ in range(self.n + 1)]
        return self.rec(0, 1, 0)
