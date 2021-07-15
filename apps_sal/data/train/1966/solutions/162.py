# create integral sum with each row, reset at 0
# In the row i, number of rectangles between column j and k(inclusive) and ends in row i, is equal to SUM(min(nums[j, .. idx])) where idx go from j to k.

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        res = 0
        m = mat
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if j > 0 and mat[i][j] == 1: #!j>0
                    m[i][j] = m[i][j - 1] + 1
        
        for j in range(len(mat[0])):
            for i in range(len(mat)):
                mn = m[i][j]

                for k in range(i, -1, -1): # from i to top  
                    mn = min(mn, m[k][j])
                    if mn == 0:
                        break
                    res += mn  #!每看到一个非零，都要加
        return res
                    
        
                

