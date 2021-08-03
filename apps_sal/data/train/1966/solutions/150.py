class Solution:
    def numSubmat1(self, mat: List[List[int]]) -> int:
        m, n, res = len(mat), len(mat[0]), 0
        histogram = [0] * (n)
        for i in range(m):
            stack, dp = [], [0] * (n)
            for j in range(n):
                histogram[j] = 0 if mat[i][j] == 0 else histogram[j] + 1
                while stack and histogram[j] < histogram[stack[-1]]:  # increasing stack
                    stack.pop()
                if stack:
                    dp[j] = dp[stack[-1]] + histogram[j] * (j - stack[-1])  # Important!!
                else:
                    dp[j] = histogram[j] * (j + 1)
                stack.append(j)
            res += sum(dp)
            print(res)
        return res

    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        count = 0
        hist = [0] * (n)
        for i in range(m):

            dp = [0] * n
            for j in range(n):
                if mat[i][j] == 1:
                    hist[j] += 1
                else:
                    hist[j] = 0
            stack = []
            for j, h in enumerate(hist):
                while stack and hist[stack[-1]] >= h:
                    stack.pop()
                if stack:
                    dp[j] = dp[stack[-1]] + hist[j] * (j - stack[-1])
                else:
                    dp[j] = hist[j] * (j + 1)
                stack.append(j)
            count += sum(dp)
            print(count)
        return count
