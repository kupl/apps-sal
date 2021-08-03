class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        arr = [0] * len(intervals)
        for i in range(len(intervals)):
            for j in range(len(intervals)):
                if(i != j and arr[j] != -1):
                    if(intervals[i][0] >= intervals[j][0] and intervals[i][1] <= intervals[j][1]):
                        arr[i] = -1
                        break
        ans = 0
        for i in arr:
            if(i != -1):
                ans += 1
        return ans
