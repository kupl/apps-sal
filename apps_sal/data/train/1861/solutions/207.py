class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        st = set()
        for (x, y) in points:
            st.add((x, y))
        minarea = float('Inf')
        for (i, p1) in enumerate(points):
            for p2 in points[:i]:
                (x1, y1) = p1
                (x2, y2) = p2
                if x1 != x2 and y1 != y2 and ((x1, y2) in st) and ((x2, y1) in st):
                    minarea = min(minarea, abs(x1 - x2) * abs(y1 - y2))
        return minarea if minarea < float('Inf') else 0
