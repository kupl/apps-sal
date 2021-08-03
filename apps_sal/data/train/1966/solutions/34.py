class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        ans = 0
        for left in range(n):
            row_sum = [0 for _ in range(m)]
            for right in range(left, n):
                consec_count = 0
                w = right - left + 1
                for bottom in range(m):
                    row_sum[bottom] += mat[bottom][right]
                    if row_sum[bottom] != w:
                        consec_count = 0
                    else:
                        consec_count += 1
                        ans += consec_count
        return ans
