class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        d = collections.defaultdict(set)
        for i in range(len(points)):
            x0, y0 = points[i]
            for j in range(i+1, len(points)):
                x1, y1 = points[j]
                if x0 == x1:
                    d[x0].add(tuple(sorted([y0,y1]))) # sorted ys since later we will use it to match
        seen = set()
        minA = float('inf')
        for x0, lines0 in d.items(): 
            seen.add(x0)
            for x1, lines1 in d.items():
                if x1 not in seen:
                    for l in lines0:
                        if l in lines1: # matching ys, that's why we sort it earlier
                            minA = min(minA, abs(x0-x1)*(l[1]-l[0]))
        return minA if minA<float('inf') else 0
