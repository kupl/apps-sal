class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        ptmap = {}
        min_area = float('inf')
        for x1, y1 in points:
            for x2, y2 in ptmap:
                if ((x1, y2) in ptmap) and ((x2, y1) in ptmap):
                    area = abs(x2 - x1) * abs(y2 - y1)
                    min_area = min(area, min_area)
            ptmap[(x1, y1)] = (x1, y1)
        return min_area if min_area != float('inf') else 0
