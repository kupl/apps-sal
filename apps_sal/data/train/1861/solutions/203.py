from collections import defaultdict


class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        mapper = defaultdict(set)
        for point in points:
            mapper[point[1]].add(point[0])
        result = float('inf')
        for (y1, x_values1) in list(mapper.items()):
            for (y2, x_values2) in list(mapper.items()):
                if y1 == y2:
                    continue
                intersect = x_values1.intersection(x_values2)
                if len(intersect) < 2:
                    continue
                x_min_diff = self.min_diff(list(intersect))
                temp = x_min_diff * abs(y1 - y2)
                if temp < result:
                    result = temp
        return result if result != float('inf') else 0

    def min_diff(self, given: list) -> int:
        result = float('inf')
        for i in range(len(given)):
            for j in range(i + 1, len(given)):
                diff = abs(given[i] - given[j])
                if diff < result:
                    result = diff
        return result
