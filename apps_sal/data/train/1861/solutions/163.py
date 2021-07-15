class Solution:
    def minAreaRect(self, points):
        pSet, ans = set(map(tuple, points)), float('inf')
        for i, (p1x, p1y) in enumerate(points):
            for (p2x, p2y) in points[i+1:]:
                if (p1x != p2x) and (p1y != p2y) and ((p1x, p2y) in pSet) and ((p2x, p1y) in pSet):
                    ans = min(ans, abs((p1x - p2x) * (p1y - p2y)))
        return ans if ans < float('inf') else 0
    

