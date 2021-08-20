class Solution:

    def stoneGameII(self, piles: List[int]) -> int:
        mem = {}

        def dp(i, M):
            if (i, M) in mem:
                return mem[i, M][0]
            if i >= len(piles):
                return 0
            val = []
            for x in range(1, min(2 * M, len(piles) - i) + 1):
                val.append(sum(piles[i:i + x]) - dp(i + x, max(x, M)))
            mem[i, M] = [max(val), val.index(max(val))]
            return mem[i, M][0]
        dp(0, 1)
        (i, m, s, t) = (0, 1, 0, 1)
        while i < len(piles):
            x = mem[i, m][1] + 1
            if t == 1:
                s += sum(piles[i:i + x])
            t *= -1
            i = i + x
            m = max(x, m)
        return s
