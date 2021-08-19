class Solution:

    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        if K == 0:
            return mat.copy()
        answers = []
        dp = []
        for row in mat:
            answers.append(row.copy())
            dp.append(row.copy())
        count = mat[0][0]
        for j in range(1, len(mat[0])):
            count += mat[0][j]
            dp[0][j] = count
        for i in range(1, len(mat)):
            count = 0
            for j in range(len(mat[0])):
                count += mat[i][j]
                dp[i][j] = count + dp[i - 1][j]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                x_outer = i + K if i + K < len(mat) - 1 else len(mat) - 1
                y_outer = j + K if j + K < len(mat[0]) - 1 else len(mat[0]) - 1
                total = dp[x_outer][y_outer]
                if i - K > 0 and j - K > 0:
                    total += dp[i - K - 1][j - K - 1]
                if j - K > 0:
                    total -= dp[x_outer][j - K - 1]
                if i - K > 0:
                    total -= dp[i - K - 1][y_outer]
                print((i, j, [i - K - 1, j - K - 1], [x_outer, y_outer], total))
                answers[i][j] = total
        print(dp)
        return answers
