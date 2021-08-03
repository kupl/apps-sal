class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        setPts = set(map(tuple,points))
        ans = sys.maxsize
        for p in range(len(points)):
            for i in range(p):
                p1 = points[p]
                p2 = points[i]
                if p1[0] != p2[0] and p1[1] != p2[1] and \\
                ((p1[0],p2[1]) in setPts and (p2[0],p1[1]) in setPts):
                    ans = min(ans,abs(p1[0]-p2[0]) * abs(p1[1]-p2[1]))
                        
        return ans if ans < sys.maxsize else 0
