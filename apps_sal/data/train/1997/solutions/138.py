class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        elif len(intervals) == 1:
            return 1

        remove_indices = []
        for i in range(len(intervals)):
            a, b = intervals[i]
            for j in range(i + 1, len(intervals)):
                c, d = intervals[j]
                if a != c or b != d:
                    if a >= c and b <= d:
                        remove_indices.append(i)
                        break
                    elif c >= a and d <= b:
                        remove_indices.append(j)

        return len([intervals[i] for i in range(len(intervals)) if i not in remove_indices])
