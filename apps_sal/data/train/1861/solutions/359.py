class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        pointset = {tuple(i) for i in points}
        ans = float('inf')

        def area(x, y):
            return abs((x[0] - y[0]) * (x[1] - y[1]))
        for (i, A) in enumerate(points):
            for j in range(i):
                B = points[j]
                if A[0] == B[0] or A[1] == B[1]:
                    continue
                if (A[0], B[1]) in pointset and (B[0], A[1]) in pointset:
                    ans = min(ans, area(A, B))
        return ans if ans != float('inf') else 0
