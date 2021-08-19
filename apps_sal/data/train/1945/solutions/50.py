class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        memo = collections.defaultdict(lambda: 0)
        M = len(matrix)
        N = len(matrix[0])
        for line in matrix:
            if line[0] == 0:
                memo[tuple(line)] += 1
            else:
                line = [1 if i == 0 else 0 for i in line]
                memo[tuple(line)] += 1
        return max(memo.values())

#         print (dict(memo))
#         # return 0
#         res = 0
#         for key, val in memo.items():
#             res = max(res, val)
#             # if key[0]==0 or key[1]==0 or key[0]==key[1]:
#             #     res = max(res, val)
#             if key[0]!=key[1] and (key[1], key[0]) in memo and  memo[(key[1], key[0])]!=0:
#                 res = max(res, memo[key]+memo[(key[1], key[0])])
#             # else:
#             #     res = max(res, val)
#         return res
