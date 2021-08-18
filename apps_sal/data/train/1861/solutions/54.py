from collections import defaultdict


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:

        points.sort(key=lambda x: (x[0], x[1]))

        heights = defaultdict(list)
        for point in points:
            x, h = point
            heights[x].append(h)

        segments = {}
        keys = list(heights.keys())
        keys.sort()
        min_area = float('inf')

        for x in keys:
            heights_x = heights[x]
            if len(heights_x) < 2:
                continue

            for i in range(len(heights_x) - 1):
                for j in range(i + 1, len(heights_x)):
                    pair = (heights_x[i], heights_x[j])
                    if pair not in segments:
                        segments[pair] = [None, x]
                    else:
                        height_diff = heights_x[j] - heights_x[i]
                        width_diff = x - segments[pair][1]
                        area = height_diff * width_diff
                        min_area = min(min_area, area)
                        segments[pair] = [segments[pair][1], x]

        if min_area == float('inf'):
            return 0
        else:
            return min_area
