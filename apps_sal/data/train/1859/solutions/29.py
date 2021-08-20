class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        rownum = len(matrix)
        if rownum < 1:
            return 0
        colnum = len(matrix[0])
        if colnum < 1:
            return 0
        aux3 = defaultdict(lambda: -1)

        def check(r, c):
            if r < 0 or r >= rownum or c < 0 or (c >= colnum):
                return 0
            elif matrix[r][c] == 0:
                return 0
            elif aux3[r, c] != -1:
                return aux3[r, c]
            else:
                c1 = check(r + 1, c)
                c2 = check(r, c + 1)
                c3 = check(r + 1, c + 1)
                aux3[r, c] = min(c1, c2, c3) + 1
                return aux3[r, c]
        ret = 0
        for r in range(0, rownum):
            for c in range(0, colnum):
                if matrix[r][c] == 1:
                    max_len = check(r, c)
                    ret += max_len
        return ret
