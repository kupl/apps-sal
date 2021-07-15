class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
      def l1(p1, p2):
        xi, yi = p1
        xj, yj = p2
        return abs(xi-xj) + abs(yi-yj)
      
      inf = float('inf')
      LV = len(points)
      E = [(u, v) for u in range(LV) for v in range(LV) if u != v]
      E = sorted(E, key=lambda x: l1(points[x[0]],points[x[1]]))
      parent = []
      
      def make_set(v):
        parent[v] = v
      
      def find_set(v):
        if v == parent[v]:
          return v
        parent[v] = find_set(parent[v])
        return parent[v]
      
      def union_sets(a, b):
        a = find_set(a)
        b = find_set(b)
        if a != b:
          parent[b] = a
          
      for v in range(LV):
        parent.append(0)
        make_set(v)
      
      F=[]
      cost = 0
      for (u,v) in E:
        if (a:=find_set(u)) != (b:=find_set(v)):
          F.append((u,v))
          cost += l1(points[u],points[v])
          union_sets(a,b)
      
      return cost
