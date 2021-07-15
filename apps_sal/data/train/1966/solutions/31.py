class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m,n = len(mat), len(mat[0])

        
        def compute(h):
          res = 0
          temp = 0 
          for i in range(len(h)):
             if h[i] > 0:
                temp += 1
             else:
                temp = 0
             res += temp
          return res 

        ans = 0 
        for i in range(m):
          h = [1]*n 
          for k in range(i,m):
            for j in range(n):
                 if mat[k][j] == 0:
                    h[j] = 0 
            ans += compute(h)
        return ans   
        

class Solution1:
    def numSubmat(self, mat: List[List[int]]) -> int:
        def countonerow(A):
            res,length = 0,0
            for i in range(len(A)):
                length = 0 if A[i] == 0 else length + 1
                res += length
            return res 
        
        def compute_one_row(arr):
            count = 0
            length = 0
            for a in arr:
                if a == 1:
                    length += 1
                else:
                    length = 0 
                count += length
            return count 
        
        m,n = len(mat), len(mat[0])
        res = 0
        for i in range(m):
            h = [1]*n
            for j in range(i,m):
                for k in range(n):
                    if mat[j][k] == 0:
                        h[k] = 0 
                res += compute_one_row(h)
        return res



    def numSubmat1(self, mat: List[List[int]]) -> int:
        m,n,res=len(mat),len(mat[0]),0
        histogram=[0]*(n+1)
        for i in range(m):
            stack,dp=[-1],[0]*(n+1)
            for j in range(n):
                histogram[j]=0 if mat[i][j]==0 else histogram[j]+1
                while histogram[j]<histogram[stack[-1]]: #increasing stack
                    stack.pop()
                dp[j]=dp[stack[-1]]+histogram[j]*(j-stack[-1]) # Important!!
                stack.append(j)
            res+=sum(dp)
        return res
