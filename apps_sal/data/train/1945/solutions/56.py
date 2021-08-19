class Solution:

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        seen = set()
        n = len(matrix)
        ans = 0
        for i in range(n):
            m = 0
            for j in range(i, n):
                if j in seen:
                    continue
                if matrix[i] == matrix[j] or all((a != b for (a, b) in zip(matrix[i], matrix[j]))):
                    seen.add(j)
                    m += 1
                    ans = max(ans, m)
        return ans
