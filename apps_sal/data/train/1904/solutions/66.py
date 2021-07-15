import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def distance(point):
            return (point[0] ** 2 + point[1] ** 2)
        
        return sorted(points, key=distance)[:K]
        
#         h = []
#         for i, p in enumerate(points):
#             if len(h) == K:
#                 heapq.heappushpop(h, (distance(p), i, p))
#             else:
#                 heapq.heappush(h, (distance(p), i, p))
                
#         out = []
#         for tup in h:
#             out.append(tup[2])
            
#         return out

