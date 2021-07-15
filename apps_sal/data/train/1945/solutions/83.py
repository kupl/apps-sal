class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        map = collections.defaultdict(int)
        for i in range(n):
            origin = \"\".join([str(j) for j in matrix[i]])
            reverse = \"\".join([str(1-j) for j in matrix[i]])
            map[origin] += 1
            map[reverse] += 1
        return max(map.values())
