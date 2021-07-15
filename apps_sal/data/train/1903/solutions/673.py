class UF:
  def __init__(self, n):
    self.parent = {i:i for i in range(n)}

  def find(self, x):
    if self.parent[x] != x:
      self.parent[x] = self.find(self.parent[x])
    return self.parent[x]
  
  def union(self, a, b):
    r_a = self.find(a)
    r_b = self.find(b)
    if r_a == r_b:
      return False
    
    self.parent[r_a] = r_b
    return True
    
  
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
      n = len(points)
      edges = []
      for i in range(n):
        for j in range(i):
          dis = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
          edges.append((dis, i, j))
      edges.sort()
      count = 0
      uf = UF(n)
      
      for dis, u, v in edges:
        if uf.union(u, v):
          count += dis
      return count
