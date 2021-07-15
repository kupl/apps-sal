class Solution:
    
    
    def singlePointSubmat(self,mat,x,y):
        row = len(mat)
        column = len(mat[0])
        
        res = 0
        
        #stoplength store the first zero position\\
        
        stoplength = column - y
        for r in range(row - x):
            if mat[x+r][y] == 1:
                res += 1
            else:
                return res
            for c in range(1,column - y):
                if c >= stoplength:
                    break
                if mat[x+r][y+c] == 1:
                    res += 1
                else:
                    stoplength = c
        return res
                    
    def numSubmat(self, mat: List[List[int]]) -> int:
        
        #check validity
        if len(mat) == 0 or len(mat[0]) == 0:
            return 0
        
        #find border
        
        row = len(mat)
        column = len(mat[0])
        
        result = 0
        
        for r in range(row):
            for c in range(column):
                
                if mat[r][c] == 1:
                    result += self.singlePointSubmat(mat,r,c)
        return result
