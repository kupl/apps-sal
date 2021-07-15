class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        for i in range(len(intervals)):
            for j in range(i, len(intervals)):
                if i == j or type(intervals[i][0]) == str or type(intervals[j][0]) == str:
                    continue
                elif intervals[i][0] >= intervals[j][0] and intervals[i][1] <= intervals[j][1]:
                    intervals[i] = ['', '']
                elif intervals[j][0] >= intervals[i][0] and intervals[j][1] <= intervals[i][1]:
                    intervals[j] = ['', '']
        interval = []
        for ele in intervals:
            if ele != ['', '']:
                interval.append(ele)
        return len(interval)

