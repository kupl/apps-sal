class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        res = 0
        for i in range(n):
            for j in range(m):

                done = False
                end_i = i
                end_j = j

                while 0 <= end_i < n and 0 <= end_j < m and not done:
                    #  check the squre of [i, new_i] * [j, new_j]
                    area = 0
                    for k in range(i, end_i + 1):
                        area += matrix[k][end_j]
                    for k in range(j, end_j + 1):
                        area += matrix[end_i][k]
                    area -= matrix[end_i][end_j]

                    if area == end_j - j + end_i - i + 1:
                        res += 1
                        end_i += 1
                        end_j += 1
                    else:
                        done = True
        return res
