class Solution:
#     def minAreaRect(self, points: List[List[int]]) -> int:
#         columns = collections.defaultdict(list)
#         for x, y in points:
#             columns[x].append(y)
#         lastx = {}
#         ans = float('inf')
        
#         for x in sorted(columns):
#             column = columns[x]
#             column.sort()
#             for index_j, y2 in enumerate(column):
#                 for index_i in range(index_j):
#                     y1 = column[index_i]
#                     if (y1, y2) in lastx:
#                         ans = min(ans, (x - lastx[(y1, y2)])* (y2 - y1))
#                     lastx[(y1, y2)] = x
#         return ans if ans < float('inf') else 0

    def minAreaRect(self, points):
        S = set(map(tuple, points))
        ans = float('inf')
        for index_j, p2 in enumerate(points):
            for index_i in range(index_j):
                p1 = points[index_i]
                if p1[0] != p2[0] and p1[1] != p2[1]:
                    if (p1[0], p2[1]) in S and (p2[0], p1[1]) in S:
                        ans = min(ans, abs((p1[0] - p2[0]) * (p1[1] - p2[1])))
            
        return ans if ans < float('inf') else 0
