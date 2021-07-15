class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        n = len(points)
        nx, ny = len(set(x for x, _ in points)), len(set(y for _, y in points))
        
        if nx == n or ny == n:
            return 0
        p = collections.defaultdict(list)
        if nx > ny:
            for x, y in points:
                p[x].append(y)
        else:
            for x, y in points:
                p[y].append(x)
        
        res = float('inf')
        dic_last = {}
        for x1, x2 in itertools.combinations(p, 2):
            if (len(p[x1]) < 2 or len(p[x2]) < 2):
                continue
            l1, l2 = sorted(p[x1]), sorted(p[x2])
            i = j = 0
            y = []
            while i < len(l1) and j < len(l2):
                v = max(l1[i], l2[j])
                if l1[i] < v:
                    i += 1
                elif l2[j] < v:
                    j += 1
                else:
                    y += v,
                    i, j = i + 1, j + 1
            
            for y1, y2 in itertools.combinations( y , 2 ):
                res = min(res, abs(x1-x2) * (y2 - y1))
        # for x in sorted(p):
        #     # print(x)
        #     p[x].sort()
        #     for y1, y2 in itertools.combinations(p[x], 2):
        #         if (y1, y2) in dic_last:
        #             res = min(res, abs( x - dic_last[y1, y2]) * abs(y1 -y2))
        #             # if res == 2:
        #             #     print(x, dic_last[y1, y2],  y1, y2)
        #         dic_last[y1, y2] = x
        return res if res < float('inf') else 0
        
        # n = len(points)
        # nx, ny = len(set(x for x, y in points)), len(set(y for x, y in points))
        # if nx == n or ny == n:
        #     return 0
        
        # p = collections.defaultdict(list)
        # if nx > ny:
        #     for x, y in points:
        #         p[x].append(y)
        # else:
        #     for x, y in points:
        #         p[y].append(x)
        # res = float('inf')
        # dic = {}
        # for x in sorted(p):
        #     p[x].sort()
        #     for y1, y2 in itertools.combinations(p[x], 2):
        #         if (y1, y2) in dic:
        #             res = min(res, abs(x - dic[y1, y2]) * abs(y1 - y2) )
        #         dic[y1, y2] = x
        # return res if res < float('inf') else 0
#         dic_x = {}
        
#         n = len(points)
#         nx, ny = len( set(x for x, y in points) ), len( set(y for x, y in points) )
#         if nx == n or ny == n:
#             return 0
        
#         p = collections.defaultdict(list)
#         if nx > ny:
#             for x, y in points:
#                 p[x].append(y)
#         else:
#             for x, y in points:
#                 p[y].append(x)
#         res = float('inf')
#         for x in sorted(p):
#             p[x].sort()
            
#             for y1, y2 in itertools.combinations(p[x], 2):
#                 # y1, y2 = p[x][i], p[x][j]
#                 if (y1, y2) in dic_x:
#                     res = min(res, abs(x - dic_x[y1, y2]) * abs(y1 -y2))
#                 dic_x[y1, y2] = x
#         return res if res < float('inf') else 0
#         seen = set()
        
#         res = float('inf')
#         for x1, y1 in points:
#             for x2, y2 in seen:
#                 if (x1, y2) in seen and (x2, y1) in seen:
#                     area = abs(x1 - x2) * abs(y1 - y2)
#                     if area and res > area:
#                         res = area
#                     # res = min(res, )
#             seen.add((x1, y1))
#         return res if res < float('inf') else 0

