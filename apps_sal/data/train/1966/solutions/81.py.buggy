class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        n=len(mat)
        m=len(mat[0])
        
        for i in range(n):
            for j in range(m-2,-1,-1):
                
                if mat[i][j]:
                    mat[i][j]+=mat[i][j+1]
                    
                    
        ans=0
        
        for i in range(n):
            for j in range(m):
                mini=float(\"inf\")
                for k in range(i,n):
                    mini=min(mini,mat[k][j])
                    
                    ans+=mini
                    
        return ans
                    
        
        
        
        
        
