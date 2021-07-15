class Solution:
    def maxEqualRowsAfterFlips(self, m: List[List[int]]) -> int:
        m=[tuple(i) for i in m]
        h=defaultdict(int)
        for i in m:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
            t=tuple(1-x for x in i)
            if t in h:
                h[t]+=1
            else:
                h[t]=1
        return max(h.values())
