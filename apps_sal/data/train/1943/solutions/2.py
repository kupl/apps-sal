class Solution:

    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = []
        while A and B:
            (start1, end1) = (A[0][0], A[0][1])
            (start2, end2) = (B[0][0], B[0][1])
            if end1 <= end2:
                if start2 <= start1:
                    res.append([start1, end1])
                elif start2 <= end1:
                    res.append([start2, end1])
                A = A[1:]
            else:
                if start1 <= start2:
                    res.append([start2, end2])
                elif start1 <= end2:
                    res.append([start1, end2])
                B = B[1:]
        return res
