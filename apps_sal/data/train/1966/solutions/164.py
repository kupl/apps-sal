class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        up = [[0]*n for _ in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if not mat[i][j]:
                    continue
                   
                if i == 0:
                    up[i][j] =  1
                else:
                    up[i][j] = up[i-1][j] + 1 
                    
                k = j 
                min_height = up[i][j]
                while k >= 0 and mat[i][k]:
                    min_height = min(min_height, up[i][k])
                    count += min_height
                    k -= 1 
                    
                
        return count 
        
        
                
            
                
                    
        
                
                

