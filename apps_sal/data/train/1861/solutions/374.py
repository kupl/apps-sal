class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
#         # N = 500 is really loose.
#         # Just check all pairs of points.
#         # Time O(N^2) , 1000ms ~ 1200ms
        
#         seen = set()
#         minA = float('inf')
#         for x1, y1 in points:
#             for x2, y2 in seen:
#                 if (x1,y2) in seen and (x2,y1) in seen:
#                     area = abs(x1-x2)*abs(y1-y2)
#                     minA = min(minA, area)
#             seen.add((x1,y1))
#         return minA if minA<float('inf') else 0
    
        # Below is a bit more ugly solution but is easier to understand
        # time is O(N^2)
        # similar question #963. Minimum Area Rectangle II
        cache = set()
        minA = float('inf')
        for x, y in points:
            cache.add((x,y)) # hash all points for quicker lookup
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)): # for every possible pair in points
                x2, y2 = points[j]
                if (x1,y2) in cache and (x2,y1) in cache:
                    area = abs(x1-x2)*abs(y1-y2)
                    if area != 0:
                        minA = min(minA, area)
        return minA if minA<float('inf') else 0
                
                
                
                
                
                
                

