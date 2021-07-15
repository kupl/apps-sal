class Solution:   
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        valid_row_indexes = range(len(mat))
        valid_col_indexes = range(len(mat[0]))
        answer = [[0]*len(mat[0]) for _ in range(len(mat))]
        for r in valid_row_indexes:
            for c in valid_col_indexes:
                left = c-K if c-K in valid_col_indexes else None
                right = c+K+1 if c+K in valid_col_indexes else None
                answer[r][c] += sum([sum(mat[i][left:right]) for i in range(r-K, r+K+1) if i in valid_row_indexes])
        return answer                
