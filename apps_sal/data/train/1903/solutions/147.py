\"\"\"
This is a minimum spanning tree problem, which can be solved by kruskal's algo or Prim's algo.
We need to pre-compute all the possible edges' weights
\"\"\"
import heapq
from typing import Tuple
class Solution:
    def __init__(self):
      self.roots = {}
      self.ranks = {}
      
    def find(self, point: Tuple[int, int]) -> Tuple[int, int]:
      self.roots.setdefault(point, point)
      self.ranks.setdefault(point, 1)
      if point != self.roots[point]:
        self.roots[point] = self.find(self.roots[point])
      return self.roots[point]
    
    def union(self, point1: Tuple[int, int], point2: Tuple[int, int], root1: Tuple[int, int], root2: Tuple[int, int]):
      if self.ranks[root1] > self.ranks[root2]:
        self.roots[root2] = root1
      elif self.ranks[root1] < self.ranks[root2]:
        self.roots[root1] = root2
      else:
        self.roots[root1] = root2
        self.ranks[root2] += 1
      
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
      \"\"\"
      Kruskal's algo: always select the lightest edge, and use a union find to detect cycles. If there are cycles ignore that edge.
      Time:
      For minimum spanning tree, V vertices have E=V-1 edges.
        * Compute all edge weights and sort: E^2 + ElogE
        * union find: amortized O(1), need to do this for all edges, so O(V). (Yes union-find with path compession and rank by union, has amortized time O(1))
        Over all E^2 + ElogE + V
      \"\"\"
      min_cost = 0
      edge_count = 0
      all_weights = []
      for i in range(len(points)):
        for j in range(i + 1, len(points)):
          xi, yi, xj, yj = (*points[i], *points[j])
          dist = abs(xi - xj) + abs(yi - yj)
          heapq.heappush(all_weights, (dist, xi, yi, xj, yj))
      
      # print(\"all_weights: \", all_weights)
      
      while len(all_weights) > 0:
        weight, xi, yi, xj, yj = heapq.heappop(all_weights)
        rooti, rootj = self.find((xi, yi)), self.find((xj, yj))
        if rooti != rootj:
          self.union((xi, yi), (xj, yj), rooti, rootj)
          # print(\"selected: \", weight, xi, yi, xj, yj)
          min_cost += weight
          edge_count += 1
          
          if edge_count == len(points) - 1: break
      
      return min_cost
