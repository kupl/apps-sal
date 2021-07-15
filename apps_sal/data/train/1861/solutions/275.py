class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points_set = set(map(tuple, points))
        result = float(\"inf\")
        for j, p2 in enumerate(points):
            for i in range(j):
                p1 = points[i]
                if p2[0] != p1[0] and p2[1] != p1[1] and (p1[0], p2[1]) in points_set and (p2[0], p1[1]) in points_set:
                    result = min(result, abs((p2[0] - p1[0]) * (p2[1] - p1[1])))
        return result if result != float(\"inf\") else 0
