class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals)
        remove = []
        flag = True
        while flag == True:
            flag = False
            for i in range(len(sorted_intervals) - 1):
                (c, d) = (sorted_intervals[i][0], sorted_intervals[i][1])
                (a, b) = (sorted_intervals[i + 1][0], sorted_intervals[i + 1][1])
                if c <= a and b <= d:
                    remove.append([a, b])
                    flag = True
                elif a <= c and d <= b:
                    remove.append([c, d])
                    flag = True
            sorted_intervals = [x for x in sorted_intervals if x not in remove]
        return len(sorted_intervals)
