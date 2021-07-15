class Solution:
    def maxEqualRowsAfterFlips(self, matrix):
        cache = collections.defaultdict(int)
        for row in matrix:
            vals = []
            trans = []
            for c in row:
                vals.append(c)
                trans.append(1 - c)
            cache[str(vals)] += 1
            cache[str(trans)] += 1
        print(cache)
        return max(cache.values())

