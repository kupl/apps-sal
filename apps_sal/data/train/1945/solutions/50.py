class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        memo = collections.defaultdict(lambda: 0)
        M = len(matrix)
        N = len(matrix[0])
        for line in matrix:
            if line[0] == 0:
                memo[tuple(line)] += 1
            else:
                line = [1 if i == 0 else 0 for i in line]
                memo[tuple(line)] += 1
        return max(memo.values())
