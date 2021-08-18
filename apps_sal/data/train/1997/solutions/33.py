class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        seen = set()
        n = len(intervals)
        for i in range(n):
            for j in range(n):
                if j == i or j in seen:
                    continue
                st1, ed1 = intervals[i][0], intervals[i][1]
                st2, ed2 = intervals[j][0], intervals[j][1]

                if st1 <= st2 and ed2 <= ed1:
                    seen.add(j)
        return n - len(seen)
