class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        length = len(points)
        if length <= 3:
            return 0

        sets = set([])
        for point in points:
            sets.add(tuple(point))

        min_area = float('inf')
        for i in range(length - 1):
            x1, y1 = points[i]
            for j in range(i + 1, length):
                x2, y2 = points[j]
                #print(x1, y1, x2, y2)
                if x1 == x2 or y1 == y2:
                    continue
                #print((x1, y2) in sets and (x2, y1) in sets)
                if (x1, y2) in sets and (x2, y1) in sets:
                    area = abs(x1 - x2) * abs(y1 - y2)
                    # print(area)
                    if area < min_area:
                        min_area = area

        if min_area == float('inf'):
            return 0
        return min_area
