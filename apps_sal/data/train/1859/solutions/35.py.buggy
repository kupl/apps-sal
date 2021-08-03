class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        \"\"\"
        Brute force, for each position (i,j) calculate the
        number of square matrices ending at (i,j) and 
        return the total sum of all numbers for all (i,j).
        
        This would cost O(m*n*m*n) time complexity. We can speed
        this up by taking advantage of the fact that such square
        submatrices ending at (i,j) must build off of previous
        submatrices. That is if we know the number of square
        submatrices of ones at (i-1,j-1), (i,j-1) and (i-1,j)
        then we can compute the number for (i,j).
        
        Concretely, the square[i][j] must equal 
            min(
                square[i-1][j-1],
                square[i-1][j],
                square[i][j-1]
            ) + 1
        
        \"\"\"
        ans = 0
        
        m = len(matrix)
        n = len(matrix[0])
        # Cache the number of square submatrices ending at current coordinate
        dp = [0] * n
        for i in range(m):
            squares_at_ij = 0
            new_dp = [0] * n
            for j in range(n):
                if matrix[i][j] == 1:
                    squares_at_ij = min(
                        dp[j], dp[j-1] if j > 0 else 0, squares_at_ij
                    ) + 1
                else: 
                    squares_at_ij = 0
                ans += squares_at_ij
                new_dp[j] = squares_at_ij
            dp = new_dp
        return ans
