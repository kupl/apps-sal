class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        ans = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                row,col = 0,0
                if mat[i][j] == 1:
                    while row<len(mat)-i and mat[i+row][j] == 1:
                        row += 1
                    while col<len(mat[0])-j and mat[i][j+col] == 1:
                        col += 1
                    cnt,col_min = 0, col
                    for ii in range(row):
                        for jj in range(min(col_min,col)):
                            if mat[i+ii][j+jj]==1:
                                cnt += 1
                            else:
                                col_min = jj
                                break
                    print((i,j,cnt))
                    ans += cnt
        return ans

