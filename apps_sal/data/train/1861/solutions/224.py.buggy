MAX_AREA = 40000 * 40000
class Solution:
\tdef minAreaRect(self, points: List[List[int]]) -> int:
\t\tpoints_set = set()
\t\tfor x, y in points:
\t\t\tpoints_set.add((x,y))
\t\tmin_area = MAX_AREA
\t\tn = len(points)
\t\tfor i in range(n-1):
\t\t\tx1,y1 = points[i]
\t\t\tfor j in range(i+1, n):
\t\t\t\tx2,y2 = points[j]
\t\t\t\tif x1 == x2 or y1 == y2:
\t\t\t\t\tcontinue
\t\t\t\tif (x1, y2) in points_set and (x2,y1) in points_set:
\t\t\t\t\tmin_area = min(min_area, abs(x2 - x1) * abs(y2 - y1))

\t\treturn 0 if min_area == MAX_AREA else min_area

