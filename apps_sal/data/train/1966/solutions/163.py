class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        for i in range(1, len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]:
                    mat[i][j] += mat[i - 1][j]

        ans = 0
        for i in range(len(mat)):
            stack = []
            cnt = 0
            for j in range(len(mat[0])):
                while stack and mat[i][stack[-1]] > mat[i][j]:
                    last = stack.pop()
                    prev = stack[-1] if stack else -1
                    cnt -= (mat[i][last] - mat[i][j]) * (last - prev)
                cnt += mat[i][j]
                ans += cnt
                stack.append(j)

        return ans
