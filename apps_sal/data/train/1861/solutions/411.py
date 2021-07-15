class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        len_x = {x for x, y in points}
        len_y = {y for x, y in points}
        
        if len(len_x) == len(points) or len(len_y) == len(points):
            return 0
        
        memo = collections.defaultdict(list)
        if len_x > len_y:
            for x, y in points:
                memo[x].append(y)
        else:
            for x, y in points:
                memo[y].append(x)
        
        res = float('inf')
        memo2 = {}
        for i in sorted(memo):
            memo[i].sort()
            for j in range(len(memo[i])):
                for k in range(j+1, len(memo[i])):
                    if (memo[i][j], memo[i][k]) in memo2:
                        res = min(res, ((memo[i][k]-memo[i][j]) * abs(memo2[(memo[i][j], memo[i][k])] - i)))
                    
                    memo2[memo[i][j], memo[i][k]] = i
        
        return res if res < float('inf') else 0
    
    
#         n = len(points)
#         nx = len(set(x for x, y in points))
#         ny = len(set(y for x, y in points))
#         if nx == n or ny == n:
#             return 0

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

