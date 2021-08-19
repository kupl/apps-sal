class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        n = len(points)
        nx = len(set(x for x, y in points))
        ny = len(set(y for x, y in points))
        if nx == n or ny == n:
            return 0
        res = 2**31
        s = {(p[0], p[1]) for p in points}

        for i, p1 in enumerate(points):
            for j, p2 in enumerate(points[i + 1:]):
                if p1[0] != p2[0] and p1[1] != p2[1]:
                    if (p1[0], p2[1]) in s and (p2[0], p1[1]) in s:
                        res = min(res, abs(p1[1] - p2[1]) * abs(p1[0] - p2[0]))
        res = res if res < 2**31 else 0
        return res


#         p = collections.defaultdict(list)
#         if nx > ny:
#             for x, y in points:
#                 p[x].append(y)
#         else:
#             for x, y in points:
#                 p[y].append(x)

#         lastx = {}
#         res = float('inf')
#         for x in sorted(p):
#             p[x].sort()
#             for i in range(len(p[x])):
#                 for j in range(i):
#                     y1, y2 = p[x][j], p[x][i]
#                     if (y1, y2) in lastx:
#                         res = min(res, (x - lastx[y1, y2]) * abs(y2 - y1))
#                     lastx[y1, y2] = x
#         return res if res < float('inf') else 0
