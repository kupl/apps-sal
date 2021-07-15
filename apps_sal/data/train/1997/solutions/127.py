class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        removed = 0
        for i in range(len(intervals)):  # 7
            for j in range(len(intervals)):  # 7 - > 7
                if i == j:
                    continue
                print((i, j))
                a, b = intervals[i]
                c, d = intervals[j]
                if c <= a and b <= d:
                    removed += 1
                    break
        
        return len(intervals) - removed

