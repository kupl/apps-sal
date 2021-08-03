class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if len(intervals) < 2:
            return n
        condition = True
        while condition:
            indexes = []
            condition = False
            for ind0 in range(n):
                for ind1 in range(ind0 + 1, n):
                    # if intervals[ind0] covered by intervals[ind1]
                    if intervals[ind1][0] <= intervals[ind0][0] and intervals[ind0][1] <= intervals[ind1][1]:
                        indexes.append(ind0)
                        if not condition:
                            condition = True
                        break
                    # if intervals[ind1] covered by intervals[ind0]
                    elif intervals[ind0][0] <= intervals[ind1][0] and intervals[ind1][1] <= intervals[ind0][1]:
                        indexes.append(ind1)
                        if not condition:
                            condition = True

            indexes = list(set(indexes))
            for index in sorted(indexes, reverse=True):
                del intervals[index]

            n = len(intervals)
            if n < 2:
                return n
        return n
