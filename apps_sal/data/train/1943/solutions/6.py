class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        result = []
        while len(A) != 0 and len(B) != 0:
            a_start, a_end = A[0]
            b_start, b_end = B[0]
            start = max(a_start, b_start)
            end = min(a_end, b_end)
            if start > end:
                if start == a_start:
                    B = B[1:]
                else:
                    A = A[1:]
            else:
                result.append([start, end])
                if end == a_end:
                    B[0] = [start, b_end]
                    A = A[1:]
                else:
                    A[0] = [start, a_end]
                    B = B[1:]
        return result
