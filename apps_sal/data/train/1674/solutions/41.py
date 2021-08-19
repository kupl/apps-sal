class Solution:

    def helper(self, s, M, n):
        if s >= n:
            return 0
        if (s, M) in self.mem:
            return self.mem[s, M]
        (cur, best) = (0, -float('inf'))
        for x in range(1, 2 * M + 1):
            if s + x > n:
                break
            cur += self.piles[s + x - 1]
            best = max(best, cur - self.helper(s + x, max(x, M), n))
        self.mem[s, M] = best
        return best

    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        self.mem = {}
        self.piles = piles
        return (sum(piles) + self.helper(0, 1, n)) // 2
