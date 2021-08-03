class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        def covers(interval, byinterval):
            return interval[0] >= byinterval[0] and interval[1] <= byinterval[1]

        ret = 0
        for i in range(len(intervals)):
            iscovered = False
            for j in (x for x in range(len(intervals)) if x != i):
                if covers(intervals[i], intervals[j]):
                    iscovered = True
                    break
            if not iscovered:
                ret += 1
        return ret
