class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        def flipped(r):
            return [1 - c for c in r]

        d = defaultdict(int)
        for r in matrix:
            s = ''.join(map(str, r))
            d[s] += 1
            s = ''.join(map(str, flipped(r)))
            d[s] += 1
        return max(d.values())
