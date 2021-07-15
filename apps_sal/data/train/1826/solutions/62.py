class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        
        
        m = len(mat)
        n = len(mat[0])
        
        answer = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                
                lower_row = max(0, i-K)
                upper_row = min(m-1, i+K)
                left_col = max(0, j-K)
                right_col = min(n-1, j+K)
                
                total = 0
                
                for x in range(lower_row, upper_row + 1):
                    for y in range(left_col, right_col + 1):
                        total += mat[x][y]
                
                answer[i][j] = total
                
                
                
        return answer
