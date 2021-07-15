class UF:
  def __init__(self, n):
    self.parent = {i:i for i in range(n)}
  
  def find(self, a):
    if a != self.parent[a]:
      self.parent[a] = self.find(self.parent[a])
    return self.parent[a]
  
  def union(self, a, b):
    r_a = self.find(a)
    r_b = self.find(b)
    if r_a == r_b:
      return False
    self.parent[r_a] = r_b
    return True
  
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)
        for i in range(n):
          for j in range(i):
            dis = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            edges.append((dis, i, j))
        edges.sort()
        cost = 0
        uf = UF(n)
        for dis, i, j in edges:
          if uf.union(i,j):
            cost += dis
        return cost
