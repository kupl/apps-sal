class Solution:

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        patterns = collections.Counter()
        for row in matrix:
            patterns[tuple(row)] += 1
            flip = [1 - c for c in row]
            patterns[tuple(flip)] += 1
        return max(patterns.values())
    '\n    \nCounter({(0, 0, 0): 1})\n===\nCounter({(0, 0, 0): 1, (1, 1, 1): 1})\n=========\nCounter({(0, 0, 0): 1, (1, 1, 1): 1, (0, 0, 1): 1})\n=========\nCounter({(0, 0, 0): 1, (1, 1, 1): 1, (0, 0, 1): 1, (1, 1, 0): 1})\n=========\nCounter({(1, 1, 0): 2, (0, 0, 0): 1, (1, 1, 1): 1, (0, 0, 1): 1})\n=========\nCounter({(0, 0, 1): 2, (1, 1, 0): 2, (0, 0, 0): 1, (1, 1, 1): 1})\n=========\n    '
