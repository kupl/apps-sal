class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        s = set()
        for a,b in points:
            s.add((a,b))
        n = len(points)
        res = float('inf')
        for i in range(n):
            for j in range(i+1,n):
                
                a,b = points[i]
                c,d = points[j]
                if a!=c and b!=d:
                    if (a,d) in s and (c,b) in s: 
                        res = min(res, abs((a-c)*(b-d)))
        return res if res < float('inf') else 0

