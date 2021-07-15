class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        dic , seen = {} , {} 
        for i, row in enumerate(mat):
            prefix_sum = [0] * (cols + 1)
            for j, num in enumerate(row):
                prefix_sum[j] = prefix_sum[j-1] + num
            
            dic[i] = prefix_sum
            
        for i in range(rows):
            for j in range(cols):
                start_col = j-K if j-K >=0 else 0
                end_col = j+K if j+K < cols else cols-1
                start_row = i-K if i-K >=0 else 0
                end_row = i+K if i+K < rows else rows-1
                if (start_col, end_col, start_row, end_row) in seen:
                    mat[i][j] = seen[start_col, end_col, start_row, end_row]
                    continue
                res = 0
                for idx in range(start_row, end_row+1):
                    res += dic[idx][end_col]- dic[idx][start_col-1]
                mat[i][j] = res
                seen[start_col, end_col, start_row, end_row] = res
        return mat

