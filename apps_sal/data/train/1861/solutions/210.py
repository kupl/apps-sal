class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        dic = collections.defaultdict(set)
        for x, y in points:
            dic[x].add(y)
        res = float('inf')
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                if x1 == x2 or y1 == y2 or y2 not in dic[x1] or y1 not in dic[x2]:
                    continue
                else:
                    res = min(res, abs(x1 - x2) * abs(y1 - y2))
        return res if res != float('inf') else 0

