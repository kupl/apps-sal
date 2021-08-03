class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        hash_set = set(map(tuple, points))
        min_ = float('inf')

        for j, p2 in enumerate(points):
            for i in range(j):
                p1 = points[i]
                x1, y1 = p2[0], p2[1]
                x2, y2 = p1[0], p1[1]
                if x1 != x2 and y1 != y2:
                    if (x2, y1) in hash_set and (x1, y2) in hash_set:
                        min_ = min(min_, abs(x1 - x2) * abs(y1 - y2))

        if min_ == float('inf'):
            return 0

        return min_
