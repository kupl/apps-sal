class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        pointsets = set()
        for point in points:
            pointsets.add((point[0], point[1]))
        ans = float(\"inf\")
        # consider two points at diagonal
        # (x1, y1) at lower left, (x2, y2) at upper right
        # since sides are parallel to x and y axes
        # then we should also find (x1, y2) and (x2, y1)
        # if found, we can form a rectangle
        for x1, y1 in points:
            for x2, y2 in points:
                if x2>x1 and y2>y1:
                    if (x2, y1) in pointsets and (x1, y2) in pointsets:
                        area = abs(x1-x2)*abs(y1-y2)
                        ans = min(area, ans)
        return ans if ans < float(\"inf\") else 0
