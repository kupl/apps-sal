class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        s = set(map(tuple, points))
        res = float('inf')
        for i in range(len(points)-1):
            for j in range(i+1,len(points)):
                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[j][0]
                y2 = points[j][1]
                if x1!=x2 and y1!=y2 and (x1,y2) in s and (x2,y1) in s:
                    res = min (res,abs((y2-y1)*(x2-x1)))
        return res if res!=float('inf') else 0

