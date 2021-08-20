"""
939. Minimum Area Rectangle.  Medium

Given a set of points in the xy-plane, 
determine the minimum area of a rectangle
formed from these points, with sides parallel
to the x and y axes.

If there isn't any rectangle, return 0.

Example 1:
Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4

Example 2:
Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2

Note:
1 <= points.length <= 500
0 <= points[i][0] <= 40000
0 <= points[i][1] <= 40000
All points are distinct.

Accepted
55,377
Submissions
107,280

NOTE: Clarify: rectangle formed by ALL these points (convex hull)
            v. rectangle formed by ANY four distinct points
"""


class Solution:

    def minAreaRectangularHull(self, points: List[List[int]]) -> int:
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

    def minAreaRect(self, points):
        S = set(map(tuple, points))
        ans = float('inf')
        for (j, p2) in enumerate(points):
            for i in range(j):
                p1 = points[i]
                if p1[0] != p2[0] and p1[1] != p2[1] and ((p1[0], p2[1]) in S) and ((p2[0], p1[1]) in S):
                    ans = min(ans, abs(p2[0] - p1[0]) * abs(p2[1] - p1[1]))
        return ans if ans < float('inf') else 0
