class Solution:

    def isCovered(self, A, B):
        if A[0] <= B[0] and A[1] >= B[1]:
            return True
        return False

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        index = 0
        while index < len(intervals):
            delete = False
            i = intervals[index]
            for j in intervals:
                if intervals[index] == j:
                    continue
                if self.isCovered(i, j):
                    intervals.remove(j)
                    index = -1
                    break
                if self.isCovered(j, i):
                    intervals.remove(i)
                    index = -1
                    break
            index += 1
        return len(intervals)
