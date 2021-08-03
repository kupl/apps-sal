class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        results = []
        max_end = float('-inf')
        for i in intervals:
            if i[1] > max_end:
                max_end = i[1]
                if len(results) == 0 or i[0] != results[-1][0]:
                    results.append(i)
                else:
                    results[-1] = i
            print(results)
        return len(results)
