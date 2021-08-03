class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda tup: tup[1] - tup[0], reverse=True)
        covered = set()

        for i in range(len(intervals)):
            s, e = intervals[i]
            for j in range(i + 1, len(intervals)):
                s2, e2 = intervals[j]

                if s <= s2 and e2 <= e:
                    covered.add(j)

        return len(intervals) - len(covered)
