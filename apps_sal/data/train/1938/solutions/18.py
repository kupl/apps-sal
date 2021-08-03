from collections import defaultdict


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        def merge_intervals(intervals):
            if not intervals:
                return 0

            intervals.sort()
            end = intervals[0][1]
            width = end - intervals[0][0]

            for left, right in intervals:
                if left < end < right:
                    width += right - end
                    end = right
                elif left >= end:
                    width += right - left
                    end = right
            return width

        events = defaultdict(list)
        for x1, y1, x2, y2 in rectangles:
            events[y1].append((1, x1, x2))
            events[y2].append((0, x1, x2))

        events = sorted(events.items(), key=lambda x: x[0])
        intervals = []
        area = width = 0
        MOD = 10 ** 9 + 7
        last_y = events[0][0]

        for y, event in events:
            area += (y - last_y) * width
            area %= MOD

            for flag, x1, x2 in event:
                if flag:
                    intervals.append((x1, x2))
                else:
                    intervals.remove((x1, x2))
            width = merge_intervals(intervals)
            last_y = y

        return area
