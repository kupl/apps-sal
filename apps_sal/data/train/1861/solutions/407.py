class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        hor = defaultdict(list)
        ver = defaultdict(list)
        seen = set()
        area = float(\"inf\")
        for point in points:
            x, y = point
            if len(hor[y]) > 0 and len(ver[x]) > 0:
                for i in ver[x]:
                    for j in hor[y]:
                        if (j, i) in seen:
                            area = min(area, abs((x-j)*(y-i)))
            seen.add((x, y))
            ver[x].append(y)
            hor[y].append(x)
        if area != float('inf'):
            return area
        else:
            return 0
