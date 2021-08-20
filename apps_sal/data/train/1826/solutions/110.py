class Solution:

    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        (h, w) = (len(mat), len(mat[0]))
        dp = [[0 for i in range(w)] for j in range(h)]
        for y in range(h):
            for x in range(w):
                sum = 0
                for i in range(x - K if x - K >= 0 else 0, x + K + 1 if x + K + 1 <= w else w):
                    sum += mat[y][i]
                dp[y][x] = sum
        res = [[0 for i in range(w)] for j in range(h)]
        for y in range(h):
            for x in range(w):
                sum = 0
                for j in range(y - K if y - K >= 0 else 0, y + K + 1 if y + K + 1 <= h else h):
                    sum += dp[j][x]
                res[y][x] = sum
        return res
