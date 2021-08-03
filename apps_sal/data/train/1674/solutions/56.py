from functools import lru_cache


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        n = len(piles)

        @lru_cache(maxsize=None)
        def dfs(index, M):
            if 2 * M >= n - index:
                return sum(piles[index:])

            ret = float('inf')
            for X in range(1, 2 * M + 1):
                if X > n - index:
                    break
                ret = min(ret, dfs(index + X, max(X, M)))

            return sum(piles[index:]) - ret

        return dfs(0, 1)

#         def dfs(index, M, order):
#             if 2*M >= n - index:
#                 if order % 2 == 1:
#                     return sum(piles[index:]), 0
#                 else:
#                     return 0, sum(piles[index:])

#             ret = [0, 0]
#             for x in range(1, 2*M + 1):
#                 if x > n - index:
#                     break
#                 a, b = dfs(index + x, max(x, M), (order + 1) % 2)
#                 if order % 2 == 1:
#                     # a += sum(piles[index:index+x])
#                     if a > ret[0]:
#                         ret[0] = a + sum(piles[index:index+x])
#                         ret[1] = b
#                 else:
#                     if b > ret[1]:
#                         # b += sum(piles[index:index+x])
#                         ret[0] = a
#                         ret[1] = b + sum(piles[index:index+x])

#             return ret[0], ret[1]

#         return dfs(0, 1, 1)[0]
