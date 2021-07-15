class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        def checkCovered(self, A, B):
            if B[0]<=A[0] and A[1]<=B[1]:
                return True
            else:
                return False
        
        res = len(intervals)
        
        for i,interval in enumerate(intervals):
            tmp = intervals[:i]+intervals[i+1:]
            for each in tmp:
                if checkCovered(self,interval,each):
                    res-=1
                    break
        return res
