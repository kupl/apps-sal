class Solution(object):
    def minAreaRect(self, points):
        \"\"\"
        :type points: List[List[int]]
        :rtype: int
        \"\"\"
        seen = set()
        res = float('inf')
        # for point, compare with all other points that we've seen so far, a rectangle can only be formed when the two points are diagonal to each other and the other points forming the other two corners also exist. If the points are parallel you don't know if you can form a rectangle yet. If there exists two other points that form a rectangle with them you will run into them both in the future so no worries to attempt to find them right away.
        for (x1, y1) in points:
            for (x2, y2) in seen:
                if (x1, y2) in seen and (x2, y1) in seen:
                    area = abs(x2-x1) * abs(y2-y1)
                    if area < res:
                        res = area
            seen.add((x1, y1))
        return res if res != float('inf') else 0
