class Solution:
\tdef minAreaRect(self, points: List[List[int]]) -> int:
\t\tpoints.sort(key = lambda x:(x[0], x[1]))
\t\tver = collections.defaultdict(list)
\t\thor = collections.defaultdict(list)
\t\tseen = set()
\t\tres = float(\"inf\")
\t\tfor x, y in points:            
\t\t\tif len(ver[x]) > 0 and len(hor[y]) > 0:
\t\t\t\tfor i in ver[x][::-1]:
\t\t\t\t\tfor j in hor[y][::-1]:
\t\t\t\t\t\tif (j, i) in seen:
\t\t\t\t\t\t\tres = min(res, (x - j) * (y - i))
\t\t\tseen.add((x, y))
\t\t\tver[x].append(y)
\t\t\thor[y].append(x)
\t\tif res != float(\"inf\"):
\t\t\treturn res
\t\telse:
\t\t\treturn 0
