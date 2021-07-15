class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        exists = [True] * len(intervals)
        for i in range(len(intervals)-1):
            for j in range(i+1, len(intervals)):
                if exists[i] and exists[j]:
                    result = self.isCovered(intervals[i], intervals[j])
                    if result == 1:
                        exists[j] = False
                    elif result == -1:
                        exists[i] = False
                    else:
                        pass
        return sum(exists)
    def isCovered(self, a: List[int], b: List[int]) -> int:
        if a[0] <= b[0] and a[1] >= b[1]:
            return 1
        elif a[0] >= b[0] and a[1] <= b[1]:
            return -1
        else:
            return 0
        

