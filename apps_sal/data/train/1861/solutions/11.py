class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        columns = defaultdict(list)
        points = sorted(points, key=lambda x: (x[0], x[1]))
        for (x, y) in points:
            columns[x].append(y)
        most_recent = {}
        min_area = float('inf')
        for x in columns:
            column = columns[x]
            for (index, y2) in enumerate(column):
                for y1 in column[:index]:
                    if (y1, y2) in most_recent:
                        min_area = min(min_area, (y2 - y1) * (x - most_recent[y1, y2]))
                    most_recent[y1, y2] = x
        return min_area if min_area < float('inf') else 0
