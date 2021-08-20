class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        coords = {}
        for (x, y) in points:
            if x not in coords:
                coords[x] = {}
            coords[x][y] = True
        area = None
        for x1 in coords:
            for y1 in coords[x1]:
                for y2 in coords[x1]:
                    if y1 == y2:
                        continue
                    for x2 in coords:
                        if x1 == x2:
                            continue
                        if y1 in coords[x2] and y2 in coords[x2]:
                            current = abs(x1 - x2) * abs(y1 - y2)
                            if area == None or current < area:
                                area = current
        if area == None:
            return 0
        return area
