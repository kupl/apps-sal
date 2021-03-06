class Solution:

    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or len(A) == 0 or (not B) or (len(B) == 0):
            return []
        res = []
        (i, j) = (0, 0)
        while i < len(A) and j < len(B):
            start = max(A[i][0], B[j][0])
            end = min(A[i][1], B[j][1])
            if A[i][0] <= B[j][1] and B[j][0] <= A[i][1]:
                res.append([start, end])
            if A[i][1] <= B[j][1]:
                i += 1
            else:
                j += 1
        return res
