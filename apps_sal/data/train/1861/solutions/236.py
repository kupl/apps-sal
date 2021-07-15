class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        coord = {(x, y) for x, y in points}
        n = len(points)
        min_area = sys.maxsize
        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 == x2 or y1 == y2: # Not diagonal of rectangle. It's just straight line so rect area would be 0 then
                    continue
                if (x1, y2) in coord and (x2, y1) in coord:
                    min_area = min(min_area, abs((x1-x2)*(y1-y2)))
                    # print(x1, x2, y1, y2, min_area)
                
        return min_area if min_area!=sys.maxsize else 0
    
#     math.sqrt((y1-y2)**2 + (x1-x2)**2), min_area

