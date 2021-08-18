class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        mx = max(list(map(max, intervals)))
        max_from = [0] * mx
        for a, b in intervals:
            max_from[a] = max(max_from[a], b)

        mx = 0
        for i in range(len(max_from)):
            mx = max(mx, max_from[i])
            max_from[i] = mx

        cnt = len(intervals)
        for a, b in intervals:
            if max_from[a] > b or (a > 0 and max_from[a - 1] >= b):
                cnt -= 1
        return cnt
