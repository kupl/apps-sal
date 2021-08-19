class Solution:

    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        events = []
        for (x1, y1, x2, y2) in rectangles:
            events.append([x1, 0, y1, y2])
            events.append([x2, 1, y1, y2])
        events.sort(key=lambda x: (x[0], -x[1]))

        def getArea(m):
            area = 0
            prev = float('-inf')
            for (l, r) in heights:
                prev = max(prev, l)
                area += max(0, r - prev) * m
                prev = max(prev, r)
            return area
        area = 0
        prev = 0
        heights = []
        for event in events:
            (cur, close, y1, y2) = event
            area += getArea(cur - prev)
            if close:
                heights.remove((y1, y2))
            else:
                heights.append((y1, y2))
                heights.sort()
            prev = cur
        return area % mod
