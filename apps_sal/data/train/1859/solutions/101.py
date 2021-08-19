class Solution:
    def getsum(self, prefix, i, j):
        if i < 0 or j < 0:
            return 0
        else:
            return prefix[min(len(prefix), i)][min(len(prefix[0]), j)]

    def countSquares(self, matrix: List[List[int]]) -> int:

        m = len(matrix)
        n = len(matrix[0])
        dp = []
        res = 0
        for i in range(m):
            dp.append([0] * n)
        for i in range(m):
            if matrix[i][0] == 1:
                dp[i][0] = 1
                res = res + 1
        for j in range(1, n):
            if matrix[0][j] == 1:
                dp[0][j] = 1
                res = res + 1

        print(res)
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] > 0:
                    dp[i][j] = min(min(dp[i - 1][j - 1], dp[i - 1][j]), dp[i][j - 1]) + 1
                    res = res + dp[i][j]
        print(dp)
        return res


#         m=len(matrix)
#         n=len(matrix[0])
#         sumv=[]
#         prefixsum=[]
#         for i in range(m):
#             sumv.append([0]*n)
#             prefixsum.append([0]*n)

#         for j in range(n):
#             sumv[0][j]=matrix[0][j]

#         for i in range(m):
#             for j in range(n):
#                 sumv[i][j]=matrix[i][j]+sumv[i-1][j]


#         for i in range(m):
#             prefixsum[i][0]=sumv[i][0]


#         for i in range(m):
#             for j in range(n):
#                 prefixsum[i][j]=sumv[i][j]+prefixsum[i][j-1]


#         res=0

#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j]!=0:
#                     for k in range(min(i,j)+2,0,-1):

#                         area=self.getsum(prefixsum,i,j)-self.getsum(prefixsum,i-k,j)-self.getsum(prefixsum,i,j-k)+self.getsum(prefixsum,i-k,j-k)


#                         if k*k==area:

#                             res+=k
#                             break
        # return res
