class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        
        ans = 0
        M = len(mat)
        if M==0:
            return 0
        N = len(mat[0])
        
        count = [0 for _ in range(N)]
        ans = 0
        for i in range(M):
            rowcount = 0
            for j in range(N):
                if mat[i][j]==1:
                    count[j] += 1
                    rowcount += 1
                    
                    minV = 1<<30
                    for k in range(j, j-rowcount, -1):
                        minV=min(minV, count[k])
                        ans += minV
                    
                else:
                    rowcount = 0
                    count[j] = 0
                    
        return ans
                    

                

