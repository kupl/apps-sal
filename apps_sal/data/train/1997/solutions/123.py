class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        isRemoved = [False] * n
        numRemoved = 0

        for i in range(n - 1):

            for j in range(i + 1, n):
                if not isRemoved[j] and not isRemoved[i]:
                    if (intervals[i][0] <= intervals[j][0]) and (intervals[i][1] >= intervals[j][1]):  # remove j
                        isRemoved[j] = True
                        numRemoved += 1
                    elif (intervals[i][0] >= intervals[j][0]) and (intervals[i][1] <= intervals[j][1]):  # remove i
                        isRemoved[i] = True
                        numRemoved += 1
        print(isRemoved)
        return n - numRemoved
