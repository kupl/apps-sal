class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        tot = len(intervals)
        valid = [True] * len(intervals)
        for i in range(len(intervals)):
            if valid[i]:
                for j in range(len(intervals)):
                    if i == j:
                        continue
                    if valid[j] and intervals[j][0] >= intervals[i][0] and intervals[j][1] <= intervals[i][1]:
                        #print('Interval', intervals[j], 'removed by ', intervals[i])
                        valid[j] = False
                        tot -= 1
        return tot
                        

