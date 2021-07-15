class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:(x[0], x[1]))
        print(points)
        ver = collections.defaultdict(list)
        hor = collections.defaultdict(list)
        seen = set()
        res = float(\"inf\")
        for x, y in points:            
            if len(ver[x]) > 0 and len(hor[y]) > 0:
                for i in ver[x][::-1]:
                    for j in hor[y][::-1]:
                        if (j, i) in seen:
                            res = min(res, (x - j) * (y - i))
            seen.add((x, y))
            ver[x].append(y)
            hor[y].append(x)
        if res != float(\"inf\"):
            return res
        else:
            return 0
        
        #1 0 1
        #0 1 0
        #1 1 1
