class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        '''
        Find the maxmimum number of rows in rows[]
        where rows[i] = rows[i+1]
        '''
        ans = 0
        for i, r in enumerate(matrix):
            count = 0
            flip = [1 - x for x in r]
            for j in range(i, len(matrix)):
                if r == matrix[j] or flip == matrix[j]:
                    count += 1
            ans = max(ans, count)
        return ans
