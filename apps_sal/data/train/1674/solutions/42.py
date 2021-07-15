class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @lru_cache(None)
        def minimax(start, m, player):
            if start >= len(piles):
                return 0
            if player == 1:
                #Alex's turn
                return max(sum(piles[start:start + x]) + minimax(start + x ,max(x, m),2) for x in range(1, 2*m + 1))
            if player == 2:
                return min(minimax(start + x, max(x, m), 1) for x in range(1, 2*m + 1))
        # @lru_cache
        # def getsum(start, end, input):
        return minimax(0, 1, 1)
        
                
                
                
                
                
                
#         result = dict()
#         result_min = dict()
        
#         def minimax(start, M, player):
#             if start >= len(piles):
#                 return 0
#             if player == 1:
#                 # maxnum = -1
#                 if (start, M) in result:
#                     return result[(start, M)]
#                 maxnum = -1
#                 for X in range(1, 2 * M + 1):
#                     temp = minimax(start + X, max(X, M), 2) + sum(piles[start:start + X])
#                     if temp > maxnum:
#                         maxnum = temp
#                 result[(start, M)] = maxnum
#                 return maxnum
                
#             if player == 2:
#                 #minimize
#                 minnum = 10^5
#                 if (start, M) in result_min:
#                     return result_min[(start, M)]
#                 minnum = 1000000
#                 for X in range(1, 2 * M + 1):
#                     temp = minimax(start + X, max(X, M), 1)
#                     if temp < minnum:
#                         minnum = temp
#                 result_min[(start, M)] = minnum
#                 return minnum
#         res = minimax(0, 1, 1)
#         print(result)
#         print(result_min)
#         return res

