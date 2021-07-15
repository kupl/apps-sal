class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        d = {}
        for arr in matrix:
            if arr[0] == 0:
                k = \"\".join(str(a) for a in arr)
            else:
                k = \"\".join(\"1\" if a==0 else \"0\" for a in arr)
            if k in d:
                d[k] += 1
            else:
                d[k] = 1
        return max(d.values())
