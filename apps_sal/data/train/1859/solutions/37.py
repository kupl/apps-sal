class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])

        diag = 0
        mem = [0 for _ in range(n)]

        res = 0
        for i in range(n):
            mem[i] = matrix[0][i]
            res += mem[i]

        for i in range(1,m):
            for j in range(n):
                tmp = mem[j]
                if matrix[i][j] == 0: mem[j] = 0
                elif j == 0:
                    mem[j] = matrix[i][j]
                    res += mem[j]
                else:
                    mem[j] = min(diag, mem[j-1], mem[j])+1
                    res += mem[j]
                diag = tmp
        return res

