"""
939. Minimum Area Rectangle.  Medium

Given a set of points in the xy-plane,
determine the minimum area of a rectangle
formed from these points, with sides parallel
to the x and y axes.

If there isn't any rectangle, return 0.

Example 1:
Input: [[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]
Output: 4

Example 2:
Input: [[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]]
Output: 2

Note:
1 <= points.length <= 500
0 <= points[j][0] <= 40000
0 <= points[j][1] <= 40000
All points are distinct.

Accepted 55,377 / 107,280 submissions.

NOTE: Clarify: rectangle formed by ALL these points (convex hull)
            v. rectangle formed by ANY four distinct points
"""


class SolutionDefDictSort:
    """
    Runtime: 664 ms, faster than 90.46% of Python3 online submissions for Minimum Area Rectangle.
    Memory Usage: 31.7 MB, less than 20.13% of Python3 online submissions for Minimum Area Rectangle.
    """

    def minAreaRect(self, points):
        columns = collections.defaultdict(set)
        for (x, y) in points:
            columns[x].add(y)
        lastx = {}
        ans = float('inf')
        for x in sorted(columns):
            column = sorted(columns[x])
            for (j, y2) in enumerate(column):
                for i in range(j):
                    y1 = column[i]
                    if (y1, y2) in lastx:
                        ans = min(ans, (x - lastx[y1, y2]) * (y2 - y1))
                    lastx[y1, y2] = x
        return ans if ans < float('inf') else 0


class SolutionTupleSet:
    """
    Runtime: 1628 ms, faster than 38.40% in Python3.
    Memory Usage: 14.4 MB, less than 17.19% in Python3.
    """

    def minAreaRect(self, points):
        S = set(map(tuple, points))
        ans = float('inf')
        for (k, (xB, yB)) in enumerate(points):
            for j in range(k):
                (xA, yA) = points[j]
                if xA != xB and yA != yB and ((xA, yB) in S) and ((xB, yA) in S):
                    ans = min(ans, abs((xB - xA) * (yB - yA)))
        return ans if ans < float('inf') else 0

    def minAreaRectangularHull(self, points: List[List[int]]) -> int:
        """
        NOTE: Not what the question was intended to meant!
        """
        area = 0
        if points:
            (minx, miny) = points[0]
            (maxx, maxy) = points[0]
            for (x, y) in points:
                minx = min(minx, x)
                miny = min(miny, y)
                maxx = max(maxx, x)
                maxy = max(maxy, y)
            area = (maxx - minx) * (maxy - miny)
        return area


class Solution:
    pass


Solution = SolutionTupleSet
Solution = SolutionDefDictSort
