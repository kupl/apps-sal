class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 4:
          return 0
        s = set([tuple(i) for i in points])
        # print(s)
        minarea = float('inf')
        for i in range(n-1):
          for j in range(i+1, n):
            if points[i][0] != points[j][0] and points[i][1] != points[j][1]:  # not in same line horizontally and vertically
              if (points[j][0], points[i][1]) in s and (points[i][0], points[j][1]) in s:
                # print(i, j)
                minarea = min(minarea, abs(points[i][0] - points[j][0]) * abs(points[i][1] - points[j][1]))

        if minarea == float('inf'):
          return 0
        return minarea
