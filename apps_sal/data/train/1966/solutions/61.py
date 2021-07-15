class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        # similar to 1277
        # but we only look left and look up
        # then take min
        count = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    # look left
                    mat[i][j] = mat[i][j-1]+1 if j>0 else 1
                    count += mat[i][j]
                    # look up
                    # need to go up to top
                    # to count all possible recs
                    min_ones = mat[i][j]
                    for k in range(i-1, -1, -1):
                        min_ones = min(min_ones, mat[k][j])
                        count += min_ones
        return count
