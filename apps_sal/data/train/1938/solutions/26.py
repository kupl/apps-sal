class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        xs = sorted({x for x1, _, x2, _ in rectangles for x in [x1, x2]})
        index = {v: i for i, v in enumerate(xs)}
        cnt = [0] * len(index)
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append([y1, x1, x2, 1])
            events.append([y2, x1, x2, -1])
        events.sort()
        curr_y = curr_x_sum = area = 0
        for y, x1, x2, sign in events:
            area += (y - curr_y) * curr_x_sum
            curr_y = y
            for i in range(index[x1], index[x2]):
                cnt[i] += sign
            curr_x_sum = sum(x2 - x1 if c else 0 for x1, x2, c in zip(xs, xs[1:], cnt))
        return area % (10**9 + 7)
