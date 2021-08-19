class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        if not points or len(points) <= 3:
            return 0
        visited = set()
        res = float('Inf')
        for (x1, y1) in points:
            for (x2, y2) in visited:
                if (x1, y2) in visited and (x2, y1) in visited:
                    area = abs(x1 - x2) * abs(y1 - y2)
                    if area and area <= res:
                        res = area
            visited.add((x1, y1))
        return res if res != float('Inf') else 0
