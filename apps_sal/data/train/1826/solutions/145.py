class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        dp = []
        result = []
        for y in range(len(mat)):
            dp.append([])
            s = 0
            for x in range(len(mat[y])):
                s += mat[y][x]
                dp[y].append(s)

        for y in range(len(mat)):
            result.append([])
            for x in range(len(mat[y])):
                cur = 0
                for y1 in range(max(y - K, 0), min(y + K + 1, len(mat))):
                    if x - K - 1 >= 0:
                        cur -= dp[y1][x - K - 1]
                    cur += (dp[y1][len(mat[y1]) - 1] if x + K >= len(mat[y1]) else dp[y1][x + K])
                result[y].append(cur)
        return result
