from heapq import nsmallest


class Solution:
    def minFallingPathSum(self, arr) -> int:
        \"\"\"
        Given a square matrix of integers, this program uses dynamic
        programming to determine the minimum falling path sum following
        the rule that the values chosen from consecutive rows cannot be
        from the same column.

        :param arr: square matrix of integers
        :type arr: list[list[int]]
        :return: minimum falling path sum
        :rtype: int
        \"\"\"

        \"\"\"
        Initialize:
        - Number of rows (rows) and number of columns (cols) are the
          same value for a square matrix.
        - Return quickly with the result when matrix is 1 x 1. 
        \"\"\"
        rows = len(arr)
        cols = rows
        if rows == 1:
            return arr[0][0]

        \"\"\"
        Dynamic Programming:
        - Overwrite the arr matrix
        - Compute a falling path sum for each element in a row
          using the falling path sums from the previous row.
        - Use the minimum path sum from the previous row unless
          it is in the column, in which case use the second
          minimum path sum.
        - Return the minimum path sum in the bottom row as the answer.
        \"\"\"
        for row in range(1, rows):
            min_path_sum, min_path_sum_2nd = nsmallest(2, arr[row - 1])
            for col in range(cols):
                if arr[row - 1][col] == min_path_sum:
                    arr[row][col] += min_path_sum_2nd
                else:
                    arr[row][col] += min_path_sum
        return min(arr[rows - 1])

