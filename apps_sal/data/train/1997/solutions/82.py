class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        for i in range(len(intervals)):
            canFit = False
            for j in range(len(intervals)):
                if i == j: continue
                if intervals[i][0] >= intervals[j][0] and intervals[i][1] <= intervals[j][1]:
                    canFit = True
                    break
            if canFit == False:
                ans += 1
        return ans

