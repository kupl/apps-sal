class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # for each item we count how many squares there are such that this item is
        # the bottom right point in the square.
        # this is equivalent to \"what is the largest square containing this item as
        # its bottom right point\"
        # so we calculate for each item what is the largest square that contains him as the bottom right
        # point, and then sum the results

        # we calculate this using dynamic programming
        # for the first row and column, the answer is already there
        total = sum(matrix[0])

        for i in range(1, len(matrix)):
            total += matrix[i][0]
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 0:
                    continue
                matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1
                total += matrix[i][j]

        return total
