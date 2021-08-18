class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        elif len(intervals) == 1:
            return 1

        remove_indices = set()
        for i in range(len(intervals)):
            a, b = intervals[i]
            for j in range(i + 1, len(intervals)):
                c, d = intervals[j]
                if a != c or b != d:
                    if a >= c and b <= d:
                        remove_indices.add(i)
                        break
                    elif c >= a and d <= b:
                        remove_indices.add(j)
        return len(intervals) - len(remove_indices)
