import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) < 1:
          return 0
        def dist(point1, point2):
          return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
#         mat = []
#         for x, point1 in enumerate(points):
#           mat.append([])
#           for y, point2 in enumerate(points):
#             if x == y:
#               dis = float('inf') 
#             else:
#               dis = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
#             mat[-1].append(dis)
        
        
        heap = []
        connected = set([0])
        for i, point in enumerate(points):
          if i == 0:
            continue
          heapq.heappush(
            heap,
            (
              dist(point, points[0]),
              i,
              0,
            )
          )
        res = 0
        while len(connected) != len(points):
          dis, p, f = heapq.heappop(heap)
          if p not in connected:
            res += dis
            connected.add(p)
            
          for i, point in enumerate(points):
            if i == p or i in connected:
              continue
            heapq.heappush(
              heap,
              (
                dist(point, points[p]),
                i,
                p,
              )
            )
        return res
