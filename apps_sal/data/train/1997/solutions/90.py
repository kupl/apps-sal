class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        a = self.checkInterval(intervals)
        return len(a)

    def checkInterval(self, intervals) -> List[List[int]]:
        if len(intervals) == 1:
            return [intervals[0]]
        else:
            front = intervals[0]
            back = self.checkInterval(intervals[1:])
            if not back: return front
            s, e = front[0], front[1]
            irrelevant = list([interval for interval in back if interval[0] <= s and e <= interval[1]])
            if len(irrelevant): 
                return back
            filtered = list([interval for interval in back if not (s <= interval[0] and interval[1] <= e)])
            return [front] + filtered

