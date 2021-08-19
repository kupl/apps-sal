class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:

        def getArea(width):
            res = 0
            prev_low = 0
            for low, high in intervals:
                low = max(prev_low, low)
                if high > low:
                    res += (high - low) * width
                    prev_low = high
            return res

        MOD = 10**9 + 7
        # convert list of rectangles to events
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((x1, 0, y1, y2))  # in
            events.append((x2, 1, y1, y2))  # out
        events.sort(key=lambda x: (x[0], x[1]))

        # sweep to calculate area
        intervals = []
        area = 0
        prev_x = 0
        for event in events:
            cur_x, type, low, high = event
            area += getArea(cur_x - prev_x)
            if type == 1:
                intervals.remove((low, high))
            else:
                intervals.append((low, high))
                intervals.sort()
            prev_x = cur_x

        return area % MOD
