class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        rows = collections.defaultdict(list)

        points.sort()

        seen = set()

        result = float('inf')

        for x1, y1 in points:
            for x2, y2 in seen:
                if x1 < x2 and y1 < y2:
                    continue

                if (x1, y2) in seen and (x2, y1) in seen:

                    area = abs(x1 - x2) * abs(y1 - y2)
                    if area and area < result:
                        result = area
            seen.add((x1, y1))

        return result if result < float('inf') else 0
