class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        L = len(intervals)
        discard = set()
        for i in range(L):
            (x, y) = intervals[i]
            for j in range(i + 1, L):
                (a, b) = intervals[j]
                if a <= x and b >= y:
                    discard.add((x, y))
                elif x <= a and y >= b:
                    discard.add((a, b))
        return L - len(discard)
