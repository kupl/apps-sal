class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        columns = collections.defaultdict(list)
        for x, y in points:
            columns[x].append(y)
        ans = float(\"inf\")
        seen = {}
        for x in sorted(columns):
            col = sorted(columns[x])
            for j, y2 in enumerate(col):
                for i in range(j):
                    y1 = col[i]
                    key = (y1, y2)
                    if key in seen:
                        ans = min(ans, (x - seen[key]) * (y2-y1))
                    seen[key] = x
        return ans if ans < float('inf') else 0
