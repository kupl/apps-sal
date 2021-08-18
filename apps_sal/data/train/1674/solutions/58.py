class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        result = dict()
        result_min = dict()

        def minimax(start, M, player):
            if start >= len(piles):
                return 0
            if player == 1:
                if (start, M) in result:
                    return result[(start, M)]
                maxnum = -1
                for X in range(1, 2 * M + 1):
                    temp = minimax(start + X, max(X, M), 2) + sum(piles[start:start + X])
                    if temp > maxnum:
                        maxnum = temp
                result[(start, M)] = maxnum
                return maxnum

            if player == 2:
                minnum = 10 ^ 5
                if (start, M) in result_min:
                    return result_min[(start, M)]
                minnum = 1000000
                for X in range(1, 2 * M + 1):
                    temp = minimax(start + X, max(X, M), 1)
                    if temp < minnum:
                        minnum = temp
                result_min[(start, M)] = minnum
                return minnum
        res = minimax(0, 1, 1)
        print(result)
        print(result_min)
        return res
