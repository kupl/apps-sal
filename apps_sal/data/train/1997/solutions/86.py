class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        cov = 0

        def covered(first, second):
            return (first[0] <= second[0]) and (second[1] <= first[1])

        for pos, inter1 in enumerate(intervals):
            for checkpos, inter2 in enumerate(intervals):
                if pos != checkpos and covered(inter2, inter1):
                    cov += 1
                    break

        return len(intervals) - cov
