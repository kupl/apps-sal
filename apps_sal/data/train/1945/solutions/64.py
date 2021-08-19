class Solution:

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        max_count = 1
        swap_matrix = [[1 - val for val in row] for row in matrix]
        for (idx, row) in enumerate(matrix):
            count = 1
            for nxt_rw in range(idx + 1, len(matrix)):
                if matrix[nxt_rw] == row or matrix[nxt_rw] == swap_matrix[idx]:
                    count += 1
            max_count = max(count, max_count)
        return max_count
