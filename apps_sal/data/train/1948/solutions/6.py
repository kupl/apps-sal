class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        ans = 1
        for (x1, y1), (x2, y2) in itertools.combinations(points, 2):
            q = math.sqrt((x1-x2)**2+(y1-y2)**2)
            if q > 2*r + 0.00001:
                continue
            # only need to calculate a circle on one side
            # consider 1-D case
            x0 = (x1+x2)/2 + math.sqrt(r**2-(q/2)**2)*(y1-y2)/q
            y0 = (y1+y2)/2 + math.sqrt(r**2-(q/2)**2)*(x2-x1)/q
            #print(x0, x1)
            ans = max(ans, sum(1 for x, y in points if (x-x0)**2+(y-y0)**2 <= r**2 + 0.00001))
        return ans
