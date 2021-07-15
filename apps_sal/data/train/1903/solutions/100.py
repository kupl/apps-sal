class UnionFind:
  def __init__(self):
    self.father = {}
    self.size = {}

  def find(self, p):
    while self.father[p] != p:
      self.father[p] = p = self.father[self.father[p]]
    return p

  def union(self, p, q):
    self.insert(p)
    self.insert(q)

    p, q = map(self.find, (p, q))
    if p == q:
      return False

    if self.size[p] < self.size[q]:
      p, q = q, p

    self.size[p] += self.size[q]
    self.father[q] = p

    return True

  def insert(self, p):
    if p not in self.father:
      self.father[p] = p
      self.size[p] = 1

      
class Solution:
  def minCostConnectPoints(self, points: List[List[int]]) -> int:
    dis = []
    for i, (x, y) in enumerate(points):
      for u, v in points[:i]:
        dis.append((abs(x-u) + abs(y-v), (x, y), (u, v)))
    dis.sort()
    
    uf, r = UnionFind(), 0
    for d, p1, p2 in dis:
      if uf.union(p1, p2):
        r += d
    return r
