class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        return max(Counter(tuple(num^r[0] for num in r) for r in matrix).values())

