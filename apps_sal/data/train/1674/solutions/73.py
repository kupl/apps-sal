class Solution:
    # opt[M][i] = max(sum(pile[i:i+m]) + sum[piles[i:]] - opt[max(m,M)][i+m]) for all m 1->2M
    def stoneGameII(self, piles: List[int]) -> int:
        if len(piles) == 1:
            return piles[0]
        pileCount = len(piles)
        scores = [[0 for y in range(0, len(piles))] for x in range(0,len(piles))]
        # print(scores)
        for i in range(len(scores)-1, -1, -1):
            for M in range(1, len(scores[i])):
                # print(\"indexes: \" + str(i) + \" , \" + str(M))
                if i + 2*M >= pileCount:
                    scores[i][M] = sum(piles[i:])
                else:
                    m_options = [sum(piles[i:i+m]) + sum(piles[i+m:]) - scores[0 if i+m > pileCount else i+m][max(m, M)] for m in range(1, 2*M + 1)]
                    # if i == 2 and M == 1:
                    #     print(sum(piles[i:i+1]))
                    #     print(sum(piles[i+1:]))
                    #     print(scores[0 if i+1 > pileCount else i+1][max(1, M)])
                    
                    # print(m_options)
                    scores[i][M] = max(m_options)
                # print(\"score grid: \")
                # for row in scores:
                #     print(row)
        return scores[0][1]
