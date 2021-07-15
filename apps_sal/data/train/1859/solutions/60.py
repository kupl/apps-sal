class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # we count for each item, how many squares there are such that this item is 
        # the bottom right point in the square
        # this is equivalent to what is the largest square containing this item as 
        # its bottom right point
        # so we calculate for each item what is the largest square that contains him as the bottom right
        # point, and then sum all the results
        
        # we calculate this using dynamic programming
        # for the first row and column, the answer is already there
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 0:
                    continue
                matrix[i][j] = min(matrix[i - 1][j], matrix[i][j- 1], matrix[i - 1][j- 1]) + 1
        
        total = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                total+= matrix[i][j]
                
        return total

