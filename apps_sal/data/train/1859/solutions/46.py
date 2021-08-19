class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        count = 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 1:
                    print((r, c))
                    size = 0
                    notOne = False
                    while not notOne and r + size <= rows - 1 and (c + size <= cols - 1):
                        for p in range(size + 1):
                            if matrix[r + p][c + size] != 1 or matrix[r + size][c + p] != 1:
                                notOne = True
                                break
                        if matrix[r + size][c + size] != 1:
                            notOne = True
                        if not notOne:
                            count += 1
                        size += 1
                        print(size)
                        print(count)
        return count
