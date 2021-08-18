class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0
        for sx in range(m):
            for sy in range(n):
                if matrix[sx][sy] == 1:
                    ans += 1
                    for by in range(sy + 1, n):
                        if matrix[sx][by] == 1 and sx + (by - sy) < m:
                            side = by - sy
                            all_one = True
                            for x in range(sx, sx + side + 1):
                                if matrix[x][by] != 1:
                                    all_one = False
                                    break
                            if not all_one:
                                break
                            for y in range(sy, sy + side + 1):
                                if matrix[sx + side][y] != 1:
                                    all_one = False
                                    break
                            if all_one:
                                ans += 1
                            else:
                                break
                        else:
                            break
        return ans
