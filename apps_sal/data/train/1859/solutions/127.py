class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])

        sub_sol = matrix[0][:]
        row, col = sub_sol[:], [0] * m

        squares = sum(sub_sol)
        for i in range(1, n):
            sol = []
            for j in range(m):
                val = matrix[i][j]
                if j == 0:
                    col.append(val)
                else:
                    if val == 0:
                        col.append(0)
                    else:
                        col.append(col[-1] + 1)

                if val == 0:
                    row[j] = 0
                else:
                    row[j] += 1

                sol.append(min(col[-1], row[j], (1 + sub_sol[j - 1]) if j > 0 else 1))
            sub_sol = sol
            squares += sum(sub_sol)

        return squares
