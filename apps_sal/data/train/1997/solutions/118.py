class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        removed = set()
        for i in range(len(intervals)-1):
            if i in removed:
                pass
            for j in range(i+1, len(intervals)):
                if intervals[i][0] <= intervals[j][0] <= intervals[j][1] <= intervals[i][1]:
                    removed.add(j)
                elif intervals[j][0] <= intervals[i][0] <= intervals[i][1] <= intervals[j][1]:
                    removed.add(i)
                    break
        return len(intervals) - len(removed)
