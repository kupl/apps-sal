class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        M = len(mat)
        N = len(mat[0])

        mark = [[0 for _ in range(N)] for _ in range(M)]

        for m in range(M):
            for n in range(N):
                if n == 0:
                    mark[m][n] = mat[m][n]
                else:
                    mark[m][n] = mark[m][n - 1] + 1 if mat[m][n] == 1 else 0
        res = 0
        for bottom in range(M):
            for right in range(N):
                Min = mark[bottom][right]
                for upper in range(bottom + 1)[::-1]:
                    Min = min(Min, mark[upper][right])
                    res += Min

        return res


#     ## Brute Force w/ Pruning O(N^2*M^2)
#     def numSubmat(self, mat: List[List[int]]) -> int:
#         M=len(mat)
#         N=len(mat[0])
#         res=0

#         for top in range(M):
#             for left in range(N):
#                 bound=N ## to bound the right pointer
#                 for bottom in range(top,M):
#                     right=left
#                     while right<bound:
#                         if mat[bottom][right]==1:
#                             res+=1
#                             right+=1
#                         else:
#                             bound=right
#                             break
#         return res
