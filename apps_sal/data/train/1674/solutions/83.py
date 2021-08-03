class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        memo = {}

        def dft(i, m, p):
            if i >= n:
                return [0, 0]
            if (i, m, p) in memo:
                return list(memo[(i, m, p)])
            score = [0, 0]
            for x in range(1, 2 * m + 1):
                s = sum(piles[i:i + x])
                forward = dft(i + x, max(m, x), (p + 1) % 2)
                forward[p] += s
                if forward[p] > score[p]:
                    score = forward
            memo[(i, m, p)] = list(score)
            return score

        return dft(0, 1, 0)[0]
