class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda t: [t[0], t[1]])
        deleted = set()
        i = 0
        while i < len(intervals):
            boundary = tuple(intervals[i])
            if not boundary in deleted:
                j = i + 1
                stop = False
                while not stop and j < len(intervals):
                    comparedBoundary = tuple(intervals[j])
                    if comparedBoundary[0] == boundary[0]:
                        deleted.add(boundary)
                        stop = True

                    elif comparedBoundary[0] >= boundary[1]:
                        stop = True
                    elif comparedBoundary[1] <= boundary[1]:
                        deleted.add(comparedBoundary)
                    j += 1
            i += 1

        return len(intervals) - len(deleted)
