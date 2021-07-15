class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        # find all falling path?: must be TLE
        # recursive with memo: also TLE, in O(n^2) time complexity
        # helper(i, j): we are looking at jth row and its last row , we choose col: i
        
#         self.dic = {}
#         def helper(i, j):
#             if (i, j) in self.dic:
#                 return self.dic[(i, j)]
            
#             if j == len(arr) -1:
#                 res =  min(arr[-1][0:i]+arr[-1][i+1:])
#                 self.dic[(i, j)] = res
#                 return res
            
            
#             res = math.inf
            
#             for c in range(len(arr)):
#                 if c != i:
#                     res = min(res, helper(c, j+1) + arr[j][c])
#             self.dic[(i, j)] = res
#             return res
        
#         res =  helper(-1, 0)
            
#         print(self.dic)
#         return res
        \"\"\"
            try dp also square complexity...
            dp[i][j] choose jth col in ith row
        \"\"\" 
        l = len(arr)
        dp = [[0]*len(arr) for _ in range(len(arr))]
        for i in range(l):
            dp[-1][i] = arr[-1][i]
        print(dp)
        res = inf
        for i in range((l-2), -1, -1):
            for j in range(l):
                dp[i][j] = min(dp[i+1][0:j] + dp[i+1][j+1:]) + arr[i][j]
        return min(dp[0])
        
