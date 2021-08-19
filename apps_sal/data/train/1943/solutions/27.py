class Solution:

    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if len(A) == 0 or len(B) == 0:
            return []
        (a_start, a_end) = A[0]
        (b_start, b_end) = B[0]
        start = max(a_start, b_start)
        end = min(a_end, b_end)
        if start > end:
            if start == a_start:
                return self.intervalIntersection(A, B[1:])
            else:
                return self.intervalIntersection(A[1:], B)
        elif end == a_end:
            B[0] = [start, b_end]
            return [[start, end]] + self.intervalIntersection(A[1:], B)
        else:
            A[0] = [start, a_end]
            return [[start, end]] + self.intervalIntersection(A, B[1:])
