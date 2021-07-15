class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        cache = collections.defaultdict(int)
        for row in matrix:
            vals = []
            trans = []
            for c in row:
                vals.append(c)
                trans.append(1 - c)
            cache[str(vals)] += 1
            cache[str(trans)] += 1
        return max(cache.values())

