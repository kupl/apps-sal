class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        
#         columns = collections.defaultdict(list)
#         for x, y in points:
#             columns[x].append(y)
#         lastx = {}
#         ans = float('inf')

#         for x in sorted(columns):
#             column = columns[x]
#             column.sort()
#             for j, y2 in enumerate(column):
#                 for i in range(j):
#                     y1 = column[i]
#                     if (y1, y2) in lastx:
#                         ans = min(ans, (x - lastx[y1,y2]) * (y2 - y1))
#                     lastx[y1, y2] = x
#         return ans if ans < float('inf') else 0
    
    
        
        # S = set(map(tuple, points))
        S = {tuple(p) for p in points}
        
        result = float('inf')
        
        for j in range(len(points)):
            for i in range(j):
                p1 = points[i]
                p2 = points[j]
                if (p1[0] != p2[0] and p1[1] != p2[1] and
                        (p1[0], p2[1]) in S and (p2[0], p1[1]) in S):
                    result = min(result, abs(p2[0] - p1[0]) * abs(p2[1] - p1[1]))
        
        return result if result < float('inf') else 0        

        
        
        
#         min_area = float('inf')
#         same_y = {}
#         h_segments = {}
                
#         for i in range(len(points)  - 1):
#             for j in range(i + 1 , len(points)):
#                 if points[i][1] == points[j][1]:
#                     key = (min(points[i][0] , points[j][0]) , max(points[i][0] , points[j][0]) )
#                     if key not in h_segments:
#                         h_segments[key] = []
#                     h_segments[key].append(points[i][1])
                                    
#         for key in h_segments:
#             width = key[1] - key[0]
            
#             val = h_segments[key]
#             if len(val) > 1:
#                 for i in range(len(val) - 1):
#                     for j in range(i, len(val)):
#                         height = abs(val[i] - val[j])
#                         if  width > 0 and  height > 0:
#                             min_area = min(min_area , width * height)
        
#         if min_area == float('inf'):
#             return 0
                
#         return min_area

