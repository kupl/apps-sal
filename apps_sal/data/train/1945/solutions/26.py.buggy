class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        map = collections.defaultdict(int)
        for row in matrix:
            map[\"\".join([str(j) for j in row])] += 1
            map[\"\".join([str(1-j) for j in row])] += 1
        return max(map.values())
