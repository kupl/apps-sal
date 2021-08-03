class Solution:
\tdef numPoints(self, P: List[List[int]], r: int) -> int:
\t\tans = 1
\t\tfor (x1, y1), (x2, y2) in itertools.combinations(P, 2):
\t\t\td = ((x1 - x2)**2 + (y1 - y2)**2) / 4.0
\t\t\tif d > r * r:
\t\t\t\tcontinue
\t\t\tx0 = (x1 + x2) / 2.0 + (y2 - y1) * (r * r - d) ** 0.5 / (d * 4) ** 0.5
\t\t\ty0 = (y1 + y2) / 2.0 - (x2 - x1) * (r * r - d) ** 0.5 / (d * 4) ** 0.5
\t\t\tans = max(ans, sum((x - x0)**2 + (y - y0)**2 <= r * r + 0.00001 for x, y in P))
\t\treturn ans
\t\t\t

