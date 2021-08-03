class Solution:
    
    def __init__(self):
        from functools import lru_cache
        return
    
    
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        self.cache = {}
        k = K
        n, m = len(mat), len(mat[0]) if len(mat) else 0
                      
        def brute_force():
            def kernel(i, j, k):
                minx, maxx = max(i-k,0), min(i+k+1, n)
                miny, maxy = max(j-k,0), min(j+k+1, m)
                s = 0
                for ii in range(minx, maxx):
                    for jj in range(miny, maxy):
                        s += mat[ii][jj]
                return s

            ans = [[0 for j in range(m)] for i in range(n)]
            for i in range(n):
                for j in range(m):
                    ans[i][j] = kernel(i,j, k)
            return ans
        
        #return brute_force()
            
        
        def partials():
            @lru_cache
            def getrowsum(i,j,k):
                miny, maxy = max(j-k,0), min(j+k+1,m)
                # row cache also needed
                return sum([mat[i][jj] for jj in range(miny, maxy)])

            #@lru_cache
            def getcolsum(ans,i,j,k):
                if (i-1, j) in self.cache:
                    self.cache[(i,j)] = self.cache[(i-1,j)] \\
                                        - (ans[i-k-1][j] if i-k-1 >= 0 else 0) \\
                                        + (ans[i+k][j] if i+k < n  else 0)
                else:
                    minx, maxx = max(i-k,0), min(i+k+1,n)
                    self.cache[(i, j)] = sum([ans[ii][j] for ii in range(minx, maxx)])
                return self.cache[(i, j)]

            ans = [[0 for j in range(m)] for i in range(n)]
            for i in range(n):
                for j in range(m):
                    ans[i][j] = getrowsum(i,j,k)

            res = [[0 for j in range(m)] for i in range(n)]
            for i in range(n):
                for j in range(m):
                    res[i][j] = getcolsum(ans,i,j,k)
            return res
        
        return partials()

