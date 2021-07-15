class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        marea=float(\"inf\")
        pd={}
        for p in points:
            pd[(p[0],p[1])]=True
        for p1 in points:
            for p2 in points:
                if p1!=p2 and p2[0]>p1[0] and p2[1]>p1[1]:
                    if (p1[0],p2[1]) in pd and (p2[0],p1[1]) in pd:
                        marea=min(marea, (p2[0]-p1[0])*(p2[1]-p1[1]) )
        return marea if marea!=float(\"inf\") else 0
        
