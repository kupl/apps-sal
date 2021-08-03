class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        min_area = float('inf')
        seen = set()

        poi = []
        for x, y in points:
            poi.append((x, y))

        for x1, y1 in points:
            for x2, y2 in seen:
                if (x1, y2) in seen and (x2, y1) in seen:
                    area = abs(x1 - x2) * abs(y1 - y2)
                    if area and area < min_area:
                        min_area = area

            seen.add((x1, y1))

        return min_area if min_area < float('inf') else 0
