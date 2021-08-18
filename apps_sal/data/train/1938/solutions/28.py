class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        xs = sorted(set(x for x1, _, x2, _ in rectangles for x in [x1, x2]))
        xi = {v: i for i, v in enumerate(xs)}
        count = [0] * len(xs)
        lines = []

        for x1, y1, x2, y2 in rectangles:
            lines.append((y1, x1, x2, 1))
            lines.append((y2, x1, x2, -1))
        lines.sort()
        curr_y, x_sum, res = 0, 0, 0
        for y, x1, x2, sign in lines:
            res += x_sum * (y - curr_y)
            curr_y = y
            for i in range(xi[x1], xi[x2]):
                count[i] += sign

            x_sum = 0
            for i in range(len(xs) - 1):
                if count[i] > 0:
                    x_sum += xs[i + 1] - xs[i]

        return res % (10**9 + 7)
