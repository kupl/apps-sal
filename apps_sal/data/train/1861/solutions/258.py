class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        seen = set()
        res = float('inf')
        for x1,y1 in points:
            for x2,y2 in seen:
                if (x1,y2) in seen and (x2,y1) in seen:
                   
                    area = abs(x1-x2)*abs(y2-y1)
                    #print(area)
                    if area>0 and area < res:
                        res = area
            seen.add((x1,y1))
        #print(seen)
        return res if res < float('inf') else 0
