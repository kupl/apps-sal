class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        d = defaultdict(int)
        for row in matrix:
            a = \"\"
            b = \"\"
            for num in row:
                a += str(num)
                b += str(num^1)
            d[a] += 1
            d[b] += 1
            
        return max(d.values())
