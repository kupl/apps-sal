class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        #took help from discussion
        for i in range(len(mat)):
            for j in range(len(mat[0])-2, -1, -1):
                if mat[i][j] > 0:
                    mat[i][j] += mat[i][j+1]
                
        ans = 0       
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                temp = float(\"inf\")
                for k in range(i, len(mat)):
                    temp = min(temp, mat[k][j])
                    ans += temp
                    
        return ans
