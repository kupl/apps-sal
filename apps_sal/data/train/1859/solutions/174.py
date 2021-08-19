class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        (m, n) = (len(matrix), len(matrix[0]))
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


'\nBrute-force: try all submatrices. O(n^2 * m^2)\n\n0 1 1 1\n1 1 1 1\n0 1 1 1\n\n0 1 2 3\n1 2 3 4\n0 1 2 3\n\n0 1 1 1\n1 2 2 2\n0 3 3 3\n\nfirst row:\nget: 0 1 2 3\n\n\n\n\n\n\n0 1 1 1 0\n1 1 1 1 1\n1 1 1 1 1\n0 1 1 1 1\n0 1 1 1 0\n\n0 5 5 5 0\n2 4 4 4 3\n1 3 4 3 2\n0 2 2 2 1\n0 1 1 1 0\n\n0 3 2 1 0\n5 4 3 2 1\n5 4 3 2 1\n5 4 3 2 1\n0 3 2 1 0\n\nO(nm)\n\n\n\n#         right = []\n#         for row in matrix:\n#             r = []\n#             count = 0\n#             for x in row:\n#                 count = count + 1 if x else 0\n#                 r.append(count)\n#             right.append(r)\n\n        \n#         for row in range(m):\n#             count = 0\n#\n#             for col in range(n):\n#                 right[row][col] = count = count + 1 if matrix[row][col] else 0\n            \n#         for col in range(n):\n#             count = 0\n#\n#             for row in range(m):\n#                 bottom[row][col] = count = count + 1 if matrix[row][col] else 0\n\n        # for row in range(m):\n        #     for col in range(n):\n        #         count += squares[row][col]\n'
