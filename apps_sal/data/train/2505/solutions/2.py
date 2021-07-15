class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1=rec1[0]
        y1=rec1[1]
        x2=rec1[2]
        y2=rec1[3]
        
        return x1<rec2[2] and rec2[0]<x2 and y1<rec2[3] and rec2[1]<y2
