class Solution:

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        cache = collections.defaultdict(int)
        for row in matrix:
            values = []
            flips = []
            for col in row:
                values.append(col)
                flips.append(1 - col)
            cache[str(values)] += 1
            cache[str(flips)] += 1
        return max(cache.values())
