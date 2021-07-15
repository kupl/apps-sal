class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        answer = 0
        
        for r in range(len(matrix)) :
            for c in range(len(matrix[0])) :
                if r > 0 and c > 0 and matrix[r][c] > 0 : 
                    matrix[r][c] = min(matrix[r][c-1],matrix[r-1][c],matrix[r-1][c-1]) + 1
                answer += matrix[r][c]
            
        return answer
                    
                    

