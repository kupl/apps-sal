class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        columns = len(mat[0])
        count = 0
        for i in range(rows):
            for j in range(columns):
                width = columns
                for y in range(i, rows):
                    if mat[y][j] == 0:
                        break
                    for x in range(j, width):
                        if mat[y][x] == 0:
                            width = x
                            break
                        count += 1
        return count
