class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        L = len(intervals)
        rm = set()
        for i in range(L):
            for j in range(i+1,L):
                l1, r1 = intervals[i]
                l2,r2 = intervals[j]
                if l1<=l2 and r1>=r2:
                    if j not in rm:
                        rm.add(j)
                elif l1>=l2 and r1<=r2:
                    if i not in rm:
                        rm.add(i)
        return L-len(rm)
