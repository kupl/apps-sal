class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2:
            return len(intervals)
        intervals.sort(key=lambda interval: interval[0])
        start, idx = 0, 1
        removed = set()

        while start < len(intervals):
            if idx == len(intervals):
                start += 1
                idx = start + 1
                continue
            if idx in removed:
                idx += 1
                continue
            if intervals[start][1] < intervals[idx][0]:
                start += 1
                idx = start + 1
                continue
            if intervals[start][1] >= intervals[idx][1]:
                removed.add(idx)
                idx += 1
                continue
            if intervals[start][1] <= intervals[idx][1]:
                if intervals[start][0] == intervals[idx][0]:
                    removed.add(start)
                    start = idx
                idx += 1
        return len(intervals) - len(removed)
