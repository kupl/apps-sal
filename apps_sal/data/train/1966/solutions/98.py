class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        ar = [[0]*len(mat[0]) for _ in range(len(mat))]
        for i in range(len(mat)):
            c = 0
            for j in range(len(mat[0])):
                if mat[i][j]: c += 1
                else: c = 0
                ar[i][j] = c
        for r in mat:
            print(r)
        print()
        for r in ar:
            print(r)
        print()
        ans = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                x = float('inf')
                for k in range(i, len(mat)):
                    x = min(x, ar[k][j])
                    ans += x
        return ans
        
        # out = mat[0][0]
        # mat[0][0] = [mat[0][0]]*3 # [row,col,diag]
        # for i in range(1, len(mat)):
        #     if mat[i][0]:
        #         row = 1 + mat[i-1][0][0]
        #         mat[i][0] = [row, 1, 1]
        #         out += row
        #     else:
        #         mat[i][0] = [0]*3
        # for r in mat:
        #     print(r)
        # print()
        # for j in range(1, len(mat[0])):
        #     if mat[0][j]:
        #         col = 1 + mat[0][j-1][1]
        #         mat[0][j] = [1, col, 1]
        #         out += col
        #     else:
        #         mat[0][j] = [0]*3
        # for r in mat:
        #     print(r)
        # print()
        # for i in range(1, len(mat)):
        #     for j in range(1, len(mat[0])):
        #         if mat[i][j]:
        #             row, col, diag = 1 + mat[i-1][j][0], 1 + mat[i][j-1][1], 1 + min(mat[i-1][j][0], mat[i][j-1][1], mat[i-1][j-1][2])
        #             mat[i][j] = [row, col, diag]
        #             out += row + col + diag - 2 # -2 to avoid triple counting
        #         else:
        #             mat[i][j] = [0]*3
        # for r in mat:
        #     print(r)
        # return out

