class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        count = 0
        for left in range(n):
            row_sums = [0 for _ in range(m)]
            for right in range(left, n):
                consec_count = 0
                width = right - left + 1
                for bottom in range(m):
                    row_sums[bottom] += mat[bottom][right]
                    if row_sums[bottom] != width:
                        consec_count = 0
                    else:
                        consec_count += 1
                        count += consec_count
        return count
