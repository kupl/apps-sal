class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        dicts = {}
        for row in matrix:
            bin_rep = ''.join([str(x) for x in row])
            if bin_rep not in dicts:
                dicts[bin_rep] = 1
            else:
                dicts[bin_rep] += 1
            rev_bin_rep = ''.join([str(x ^ 1) for x in row])
            if rev_bin_rep not in dicts:
                dicts[rev_bin_rep] = 1
            else:
                dicts[rev_bin_rep] += 1
            #print (bin_rep, rev_bin_rep)
        res = 0
        #print (dicts)
        for key, value in dicts.items():
            res = max(res, value)
        return res
