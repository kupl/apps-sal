class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n, res = len(mat), len(mat[0]), 0
        histogram = [0] * (n + 1)
        for i in range(m):
            stack, dp = [-1], [0] * (n + 1)
            for j in range(n):
                if mat[i][j] == 0:
                    histogram[j] = 0
                else:
                    histogram[j] += 1

                while histogram[j] < histogram[stack[-1]]:
                    # print(stack)
                    stack.pop()
                    # print(stack)

                # print(stack)
                dp[j] = dp[stack[-1]] + histogram[j] * (j - stack[-1])
                stack.append(j)

            res += sum(dp)

        return res
