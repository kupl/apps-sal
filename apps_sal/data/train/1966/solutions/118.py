class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        pre = [[0] * (n + 1) for _ in range(m)]

        for row in range(m):
            for col in range(1, n + 1):
                pre[row][col] = mat[row][col - 1] + pre[row][col - 1]

        ans = 0
        for col1 in range(n):
            for col2 in range(col1 + 1, n + 1):
                local_ans = 0
                curr_stack = 0
                for row in range(m):
                    if pre[row][col2] - pre[row][col1] == col2 - col1:
                        curr_stack += 1
                        local_ans += curr_stack
                    else:
                        curr_stack = 0
                ans += local_ans
        return ans
