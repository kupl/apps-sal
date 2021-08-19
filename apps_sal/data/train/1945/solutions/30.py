class Solution:

    def maxEqualRowsAfterFlips(self, x: List[List[int]]) -> int:
        f = defaultdict(int)
        n = len(x[0])
        for i in x:
            p = q = 0
            v = 1
            for j in range(n):
                if i[j] == 0:
                    p |= v
                else:
                    q |= v
                v = v << 1
            f[p] += 1
            f[q] += 1
        return max(f.values())
