class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        
        lim1 = len(mat)
        lim2 = len(mat[0])
        
        hz = [[0 for j in range(0,lim2)] for i in range(0,lim1)]
        
        t = 0
        for i in range(lim1-1,-1,-1):
            for j in range(lim2-1,-1,-1):
                if mat[i][j]!=0:
                    if j<lim2-1:
                        hz[i][j]+=hz[i][j+1]+1
                    else:
                        hz[i][j]=1
        
        vt = [[0 for j in range(0,lim2)] for i in range(0,lim1)]
        
        for i in range(0,lim1):
            for j in range(0,lim2):
                if hz[i][j]!=0:
                    mn = 99999999999
                    for k in range(i,lim1):
                        if hz[k][j]==0:
                            break
                        else:
                            if hz[k][j]<mn:mn = hz[k][j]
                    
                        t+=mn
        
        return t
        

