from copy import deepcopy
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if matrix == [] or matrix[0] == []:
            return 0
        n, m = len(matrix), len(matrix[0])
        left = deepcopy(matrix)
        down = deepcopy(matrix)
        output = deepcopy(matrix)
        for i in reversed(list(range(n-1))):
            for j in reversed(list(range(m-1))):
                if matrix[i][j] == 1:
                    left[i][j] = left[i][j+1] + 1
                    down[i][j] = down[i+1][j] + 1
                    output[i][j] = min(left[i][j], down[i][j], output[i+1][j+1]+1)
                #print(i, j, output[i][j], left[i][j], down[i][j])
        return sum(sum(x) for x in output)

