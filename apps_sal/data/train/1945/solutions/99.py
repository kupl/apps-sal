class Solution:

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:

        def encode(row):
            (i, l) = (row[0], 0)
            result = ''
            result2 = ''
            for j in row:
                if j == i:
                    l += 1
                else:
                    result += f'{i}{l}'
                    result2 += f'{(i + 1) % 2}{l}'
                    i = j
                    l = 1
            result += f'{i}{l}'
            result2 += f'{(i + 1) % 2}{l}'
            return (result, result2)
        (m, n) = (len(matrix), len(matrix[0]))
        g = {}
        for i in range(m):
            (a, b) = encode(matrix[i])
            if a in g:
                g[a] += 1
            elif b in g:
                g[b] += 1
            else:
                g[a] = g.get(a, 0) + 1
        return max(g.values())
