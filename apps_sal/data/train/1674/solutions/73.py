class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        if len(piles) == 1:
            return piles[0]
        pileCount = len(piles)
        scores = [[0 for y in range(0, len(piles))] for x in range(0, len(piles))]
        for i in range(len(scores) - 1, -1, -1):
            for M in range(1, len(scores[i])):
                if i + 2 * M >= pileCount:
                    scores[i][M] = sum(piles[i:])
                else:
                    m_options = [sum(piles[i:i + m]) + sum(piles[i + m:]) - scores[0 if i + m > pileCount else i + m][max(m, M)] for m in range(1, 2 * M + 1)]

                    scores[i][M] = max(m_options)
        return scores[0][1]
