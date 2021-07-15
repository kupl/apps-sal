

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        xs = sorted(list(set(x for x1, y1, x2, y2 in rectangles for x in [x1, x2])))
        xs_i = {x: i for i, x in enumerate(xs)}
        
        rects = []
        for x1, y1, x2, y2 in rectangles:
            rects.append((y1, x1, x2, 1))
            rects.append((y2, x1, x2, -1))
        rects = sorted(rects)
        counts = [0] * len(xs_i)
    
        curr_y = 0
        area = 0
        L = 0
        for y, x1, x2, sig in rects:
            area += (y - curr_y) * L
            curr_y = y
            for x in range(xs_i[x1], xs_i[x2]):
                counts[x] += sig
            L = sum(x2 - x1 for x1, x2, s1 in zip(xs, xs[1:], counts) if s1 > 0 )
        return area % (10**9 + 7)
