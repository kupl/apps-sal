from itertools import combinations

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        area = float('inf')
        by_x = {}
        visited = {}
        for point in points:
            by_x[point[0]] = []
        for point in points:
            by_x[point[0]].append(point[1])
            
        for x in sorted(by_x):
            for y1, y2 in combinations(sorted(by_x[x]), 2):
                if (y1, y2) in visited:
                    area = min(area, abs(x - visited[(y1, y2)]) * abs(y2 - y1))
                visited[(y1, y2)] = x
            
        return area if area != float('inf') else 0
