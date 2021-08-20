class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        res = float('inf')
        dic = collections.defaultdict(set)
        for p in points:
            dic[p[0]].add(p[1])
        for i in range(len(points)):
            for j in range(len(points)):
                (p1, p2) = (points[i], points[j])
                if p1[0] >= p2[0] or p1[1] >= p2[1]:
                    continue
                if p1[1] in dic[p2[0]] and p2[1] in dic[p1[0]]:
                    res = min(res, (p2[0] - p1[0]) * (p2[1] - p1[1]))
        return res if res != float('inf') else 0
