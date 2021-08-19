class Solution:
    #     https://leetcode.com/problems/count-submatrices-with-all-ones/discuss/721999/Python3-O(MN)-histogram-model
    # Should pay more attention to this one
    # Histogram model. First, stack all the rows, (prefix sum vertically)
    # And then use a non-decreasing stack for each row
    # Cumulate count to res, unless lower height appears, adjust the height
    # Using non-decreasing stack and cumulative, each time, you can add current height to each of the previous same row possibility
    # We rule out the non-continuous
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        for r in range(m):
            for c in range(n):
                if mat[r][c] and r > 0:
                    mat[r][c] += mat[r - 1][c]
        res = 0
        for r in range(m):
            count = 0
            stack = []
            for c in range(n):
                while stack and mat[r][stack[-1]] > mat[r][c]:
                    j = stack.pop()
                    w = stack[-1] if stack else -1
                    count -= (mat[r][j] - mat[r][c]) * (j - w)

                count += mat[r][c]
                res += count
                stack.append(c)
        return res
