from collections import defaultdict
class Solution:
    # O(n ^ 2) Time | O(n) Space
    def minAreaRect(self, points: List[List[int]]) -> int:
        rows = defaultdict(list)
        for i, j in points:
            rows[i].append(j)
        result = float('inf')
        lastRow = {}
        for row in sorted(rows.keys()):
            cols = (rows[row])
            cols.sort()
            for j, col2 in enumerate(cols):
                for i in range(j):
                    col1 = cols[i]
                    if (col1, col2) in lastRow:
                        result = min(result, ((row - lastRow[(col1, col2)]) * (col2 - col1)))
                    lastRow[(col1, col2)] = row
        return result if result != float('inf') else 0
