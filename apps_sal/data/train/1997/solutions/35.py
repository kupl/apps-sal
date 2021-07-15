class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        I = len(intervals)
        count = 0
        covered = {}
        removed = {}
        for i in range (0, I):
            for j in range(0, I):
                if i == j:
                    continue
                if j in removed or i in removed:
                    continue
                if intervals[i][0] <= intervals[j][0] and intervals[i][1] >= intervals[j][1]:
                    if (i, j) not in covered and (j, i) not in covered:                    
                        count += 1
                        covered[(i, j)] = 1
                        covered[(j, i)] = 1
                        removed[j] = j
        return len(intervals) - count            

