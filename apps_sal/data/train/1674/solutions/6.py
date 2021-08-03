class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        for i in range(len(piles) - 2, -1, -1):
            piles[i] += piles[i + 1]

        from functools import lru_cache

        @lru_cache(None)
        def dp(index, m):
            if index >= len(piles):
                return 0
            max_val = 0

            for i in range(index, min(index + 2 * m, len(piles))):
                new_m = max(m, i + 1 - index)
                max_val = max(max_val, piles[index] - dp(i + 1, new_m))
            return max_val
        return dp(0, 1)

#         N = len(piles)
#         for i in range(N-2, -1, -1):
#             piles[i] += piles[i+1]
#         print(piles)
#         from functools import lru_cache
#         @lru_cache(None)
#         def dp(i, m):
#             if i + 2 * m >= N: return piles[i]
#             return piles[i] - min(dp(i + x, max(m, x)) for x in range(1, 2 * m + 1))
#         return dp(0, 1)
        max_num = 0

        def play(i, m, player):

            if i >= len(piles):
                return 0

            if player == 1:
                point = play(i + 2 * m, 2 * m, 0)

                return point
            else:

                max_point = 0
                for action in range(i + 1, min(i + 1 + 2 * m, len(piles))):
                    print((sum(piles[i:action]), i, m, action, piles[i:action], min(i + 1 + 2 * m, len(piles))))
                    down_stream_point = play(action, max(action, m), 1)
                    max_point = max(max_point, sum(piles[i:action]) + down_stream_point)

                return max_point

        return play(0, 1, 0)
