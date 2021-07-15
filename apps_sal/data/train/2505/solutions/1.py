class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        
        r1x1 = rec1[0]
        r1y1 = rec1[1]
        r1x2 = rec1[2]
        r1y2 = rec1[3]
        
        r2x1 = rec2[0]
        r2y1 = rec2[1]
        r2x2 = rec2[2]
        r2y2 = rec2[3]
        
        if r2x1 >= r1x2 or r1x1 >= r2x2:
            return False
        if r2y1 >= r1y2 or r1y1 >= r2y2:
            return False
        return True
