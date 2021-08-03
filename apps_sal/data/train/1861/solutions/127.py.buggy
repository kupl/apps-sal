class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        ans = float(\"inf\")
        point_set = set()
        for p in points:
            point_set.add((p[0],p[1]))
        for x1, y1 in point_set:
            for x2, y2 in point_set:
                if x1 > x2 and y1 > y2: # make sure no zero 
                    if (x1,y2) in point_set and (x2, y1) in point_set:
                        ans = min(abs((x1 - x2)) * abs((y1 - y2)), ans)
        return ans if ans != float(\"inf\") else 0
