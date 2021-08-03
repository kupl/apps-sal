class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        cnt = defaultdict(int)

        for i in range(m):
            s1, s2 = '', ''

            for j in range(n):
                s1 += str(matrix[i][j])
                s2 += str(1 ^ matrix[i][j])

            cnt[s1] += 1
            cnt[s2] += 1

        return max(list(cnt.values()))
