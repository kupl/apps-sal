class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        removed = 0
        removedSet = set()
        for ind1 in range(len(intervals)):
            for ind2 in range(len(intervals)):
                if ind1 == ind2 or ind1 in removedSet:
                    continue
                interval1 = intervals[ind1]
                interval2 = intervals[ind2]

                if interval1[0] >= interval2[0] and interval1[1] <= interval2[1]:
                    removed += 1
                    removedSet.add(ind1)

        return len(intervals) - removed
