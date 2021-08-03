def checkCovered(a, b):
    if a[0] < b[0] or a[1] > b[1]:
        return False

    return True


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        covered = [0] * len(intervals)
        for i in range(len(intervals) - 1):
            a = intervals[i]
            for j in range(i + 1, len(intervals)):
                b = intervals[j]

                if covered[i] == 0:
                    if checkCovered(a, b):
                        covered[i] = 1

                if covered[j] == 0:
                    if checkCovered(b, a):
                        covered[j] = 1

        return covered.count(0)
