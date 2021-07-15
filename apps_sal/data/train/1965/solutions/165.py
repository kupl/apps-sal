class UnionFind:
  def __init__(self, n):
    self.father = list(range(n+1))
    self.count = n
    self.size = [0] * (n + 1)
    
  def find(self, p):
    while p != self.father[p]:
      self.father[p] = p = self.father[self.father[p]]
    return p
    
  def union(self, p, q):
    p, q = map(self.find, (p, q))
    if p == q:
      return False
    if self.size[p] < self.size[q]:
      p, q = q, p
    self.father[q] = p
    self.size[p] += self.size[q]
    self.count -= 1
    return True

class Solution:
  def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
    alice, bob, result = UnionFind(n), UnionFind(n), 0
    for i in range(3, 0, -1):
      for t, u, v in edges:
        if i != t:
          continue
        if i == 3:
          x = alice.union(u, v)
          y = bob.union(u, v)
          result += not x and not y
        elif i == 2:
          result += not bob.union(u, v)
        else:
          result += not alice.union(u, v)
    return result if alice.count == 1 and bob.count == 1 else -1
