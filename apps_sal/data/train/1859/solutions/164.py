class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        max_square_size = min(m, n)
        ones = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    ones.append([i, j])
        square_count = len(ones)
        for p in ones:
            for j in range(1, max_square_size):

                found_zero = False
                for rj in range(j + 1):
                    for cj in range(j + 1):
                        try:
                            if matrix[p[0] + rj][p[1] + cj] == 0:
                                found_zero = True
                                break
                        except IndexError:
                            found_zero = True
                    if found_zero:
                        break
                if found_zero:
                    break
                else:
                    square_count += 1

        return square_count
