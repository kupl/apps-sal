import copy


class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        (m, n) = (len(matrix), len(matrix[0]))
        counter = copy.deepcopy(matrix)
        for i in range(1, m):
            for j in range(1, n):
                if counter[i][j] == 1:
                    counter[i][j] = 1 + min(counter[i - 1][j], counter[i - 1][j - 1], counter[i][j - 1])
        total_count = 0
        for i in range(m):
            for j in range(n):
                total_count += counter[i][j]
        return total_count
