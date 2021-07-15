class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        columns = len(mat[0])
        def countSubmat(s_r, s_c):
            e_r = rows
            e_c = columns
            c_r = s_r
            c_c = s_c
            count = 0
            while c_r < e_r:
                if mat[c_r][s_c] == 0:
                    break
                else:
                    count += 1
                    c_c = s_c + 1
                while c_c < e_c:
                    if mat[c_r][c_c] == 1:
                        count += 1
                    else:
                        e_c = c_c
                    c_c += 1
                c_r += 1
                c_c = s_c
            return count
        res = 0
        for i in range(rows):
            for j in range(columns):
                res += countSubmat(i, j)
        return res
                    
            

