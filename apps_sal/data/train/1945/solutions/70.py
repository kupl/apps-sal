class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        cache = defaultdict(int)
        for row in matrix:
            vals = []
            trans = []
            for num in row:
                vals.append(num)
                trans.append(1 - num)
            cache[str(vals)] += 1
            cache[str(trans)] += 1

        return max(cache.values())
