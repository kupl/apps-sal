from collections import defaultdict
class Solution:
\tdef minAreaRect(self, points) -> int:
\t\tif(len(points) < 2):
\t\t\treturn 0

\t\tpoints = set(map(tuple,points))
\t\txMap = defaultdict(list)
\t\tyMap = defaultdict(list)

\t\tfor point in points:
\t\t\tx = point[0]
\t\t\ty = point[1]
\t\t\t
\t\t\txMap[x].append(y)

\t\t\tyMap[y].append(x)

\t\tresult = float('inf')
\t\tfor x1 in xMap.keys():
\t\t\tfor i in range(len(xMap[x1])):
\t\t\t\ty1 = xMap[x1][i]
\t\t\t\tfor j in range(i+1, len(xMap[x1])):
\t\t\t\t\ty2 = xMap[x1][j]
\t\t\t\t\tfor x2 in yMap[y2]:
\t\t\t\t\t\tif(x1 < x2 and ((x2,y1) in points)):
\t\t\t\t\t\t\tresult = min(result,abs((y2-y1)*(x2-x1)))
\t\tif(result == float('inf')):
\t\t\treturn 0
\t\treturn result
