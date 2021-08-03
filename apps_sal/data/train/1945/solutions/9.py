class Solution:
    def maxEqualRowsAfterFlips(self, ma: List[List[int]]) -> int:
        n = len(ma)
        m = len(ma[0])
        di = {}
        for i in range(n):
            s = ''
            ss = ''
            for j in range(m):
                s = s + str(ma[i][j])
                ss = ss + str(1 - ma[i][j])
            di[s] = di.get(s, 0) + 1
            di[ss] = di.get(ss, 0) + 1
        return max(list(di.values()))
