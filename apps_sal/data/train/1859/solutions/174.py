class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        squares = copy.deepcopy(matrix)
        count = 0
        ones_in_col = [0] * n

        for row in range(m):
            ones_in_row = 0

            for col in range(n):
                ones_in_row = ones_in_row + 1 if matrix[row][col] else 0
                ones_in_col[col] = ones_in_col[col] + 1 if matrix[row][col] else 0
                top_left_res = 0 if row == 0 or col == 0 else squares[row - 1][col - 1]

                squares[row][col] = min(ones_in_row, ones_in_col[col], top_left_res + 1)

                count += squares[row][col]

        return count


'''
Brute-force: try all submatrices. O(n^2 * m^2)

0 1 1 1
1 1 1 1
0 1 1 1

0 1 2 3
1 2 3 4
0 1 2 3

0 1 1 1
1 2 2 2
0 3 3 3

first row:
get: 0 1 2 3






0 1 1 1 0
1 1 1 1 1
1 1 1 1 1
0 1 1 1 1
0 1 1 1 0

0 5 5 5 0
2 4 4 4 3
1 3 4 3 2
0 2 2 2 1
0 1 1 1 0

0 3 2 1 0
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
0 3 2 1 0

O(nm)




        
            

'''
