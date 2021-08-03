class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:

        if not A or not B:
            return []
        m, n = len(A), len(B)
        result = []
        i = j = 0
        while i < m and j < n:
            start = max(A[i][0], B[j][0])
            end = min(A[i][1], B[j][1])

            if start <= end:
                result.append([start, end])

            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return result
