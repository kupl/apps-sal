class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        deleted = set()
        for i in range(len(intervals)):
            for j in range(len(intervals)):
                if i != j and j not in deleted and intervals[i][0] <= intervals[j][0] < intervals[j][1] <= intervals[i][1]:
                    deleted.add(j)
        return len(intervals) - len(deleted)
