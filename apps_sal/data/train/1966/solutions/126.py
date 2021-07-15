class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        ar = [[0 for j in range(m)]for i in range(n)]
        c = 0
        for i in range(n):
            c = 0 
            for j in range(m-1,-1,-1):
                if mat[i][j] == 1:
                    c += 1
                else:
                    c = 0
                ar[i][j] = c
        
        ans = 0
        for i in range(n):
            for j in range(m):
                x = float('inf')
                for k in range(i,n):
                    x = min(x,ar[k][j])
                    ans += x
        
        return ans
