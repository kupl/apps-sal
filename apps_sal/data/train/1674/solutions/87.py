from functools import lru_cache


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        def alex(idx, M, score_alex, score_lee):
            #print('alex', idx, M, score_alex, score_lee)
            if idx == len(piles):
                return score_alex, score_lee
            if idx == len(piles) - 1:
                return score_alex + piles[idx], score_lee
            maxa, countl = score_alex, score_lee
            for i in range(1, 2 * M + 1):
                if idx + i <= len(piles):
                    sa, sl = lee(idx + i, i, score_alex + sum(piles[idx:idx + i]), score_lee)
                    if maxa < sa:
                        maxa = sa
                        countl = sl
                else:
                    break
            #print('--------> alex', idx, M, maxa, countl)
            return maxa, countl

        def lee(idx, M, score_alex, score_lee):
            #print('lee', idx, M, score_alex, score_lee)
            if idx == len(piles):
                return score_alex, score_lee
            if idx == len(piles) - 1:
                return score_alex, score_lee + piles[idx]
            counta, maxl = score_alex, score_lee
            for i in range(1, 2 * M + 1):
                if idx + i <= len(piles):
                    sa, sl = alex(idx + i, i, score_alex, score_lee + sum(piles[idx:idx + i]))
                    if maxl < sl:
                        maxl = sl
                        counta = sa
                else:
                    break
            #print('--------> lee', idx, M, maxl, counta)
            return counta, maxl

        #self.memo = dict()
        # return alex(0, 1, 0, 0)[0]

        @lru_cache(None)
        def minimax(i, m, player):
            if i >= len(piles):
                return 0
            if player == 0:
                return max(sum(piles[i:i + j]) + minimax(i + j, max(m, j), player ^ 1) for j in range(1, 2 * m + 1))
            else:
                return min(minimax(i + j, max(m, j), player ^ 1) for j in range(1, 2 * m + 1))
        return minimax(0, 1, 0)
