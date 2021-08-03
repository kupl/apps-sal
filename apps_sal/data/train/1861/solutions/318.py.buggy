from itertools import combinations

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points_s = set(map(tuple,points))
        
        ans = float(\"inf\")
        for p, q in combinations(points, 2):
            if p[0] != q[0] and p[1] != q[1]:
                if (p[0], q[1]) in points_s and (q[0], p[1]) in points_s:
                    ans = min(ans, abs(p[0] - q[0]) * abs(p[1] - q[1]))
                    
        return ans if ans < float(\"inf\") else 0
