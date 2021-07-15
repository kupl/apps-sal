class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        i1, j1, i2, j2 = rec2
        
        
        if i1 >= x2 or x1 >= i2 or y1 >= j2 or j1 >= y2:
            return False
        return True
