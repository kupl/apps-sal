class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        columns = defaultdict(list)
        for (x, y) in points:
            columns[x].append(y)
        (seen, result) = ({}, float('inf'))
        for x2 in sorted(columns):
            column = columns[x2]
            column.sort()
            for (j, y2) in enumerate(column):
                for i in range(j):
                    y1 = column[i]
                    if (y1, y2) in seen:
                        result = min(result, (x2 - seen[y1, y2]) * (y2 - y1))
                    seen[y1, y2] = x2
        return result if result != float('inf') else 0
