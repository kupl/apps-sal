class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:

        S = {tuple(p) for p in points}

        result = float('inf')

        for j in range(len(points)):
            for i in range(j):
                p1 = points[i]
                p2 = points[j]
                if (p1[0] != p2[0] and p1[1] != p2[1] and
                        (p1[0], p2[1]) in S and (p2[0], p1[1]) in S):
                    result = min(result, abs(p2[0] - p1[0]) * abs(p2[1] - p1[1]))

        return result if result < float('inf') else 0
