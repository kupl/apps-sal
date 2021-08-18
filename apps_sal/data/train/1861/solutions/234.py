class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        if len(points) < 4:
            return 0

        x_coord = collections.defaultdict(list)
        points.sort(key=lambda x: (x[0], x[1]))
        min_area = float('inf')
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 == x2:
                    if (y1, y2) in x_coord:
                        x_other = x_coord[(y1, y2)][-1]
                        min_area = min(min_area, (y2 - y1) * (x1 - x_other))
                    x_coord[(y1, y2)].append(x1)
        return min_area if min_area != float('inf') else 0
