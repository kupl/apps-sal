class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        columns = collections.defaultdict(list)
        for (x, y) in points:
            columns[x].append(y)
        ans = float('inf')
        lastx = dict()
        for x in sorted(columns):
            column = columns[x]
            column.sort()
            for (i, y2) in enumerate(column):
                for y1 in column[:i]:
                    if (y1, y2) in lastx:
                        ans = min(ans, (x - lastx[y1, y2]) * abs(y2 - y1))
                    lastx[y1, y2] = x
        return ans if ans < float('inf') else 0
