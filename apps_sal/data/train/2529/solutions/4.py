class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        res=0
        for i in range(len(mat)):
            for j in range(len(mat[-1])):
                if mat[i][j]==1 and sum(mat[i])==1 and sum(mat[o][j] for o in range(len(mat)))==1:
                    res+=1
        return res
