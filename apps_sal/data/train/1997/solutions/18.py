class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        def covered(a, b):
            return a[0] >= b[0] and a[1] <= b[1]
        deleted = set()
        for i in range(len(intervals)):
            for j in range(len(intervals)):
                if i != j and i not in deleted:
                    if covered(intervals[i], intervals[j]):
                        deleted.add(i)
        return len(intervals) - len(deleted)
