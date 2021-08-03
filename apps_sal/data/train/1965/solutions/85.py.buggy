from typing import Tuple
class Solution:
    def __init__(self):
      self.roots = {}
      self.ranks = {}
      self.groups = 0
    
    def find(self, node_info: Tuple[int, int]):
      self.roots.setdefault(node_info, node_info)
      self.ranks.setdefault(node_info, 1)
      if self.roots[node_info] != node_info:
        self.roots[node_info] = self.find(self.roots[node_info])
      return self.roots[node_info]
    
    def union(self, node_info1, node_info2) -> bool:  # returns if the edge can be removed
      root1, root2 = self.find(node_info1), self.find(node_info2)
      if root1 != root2:
        self.groups -= 1
        if self.ranks[root2] < self.ranks[root1]:
          self.roots[root2] = root1
        elif self.ranks[root1] < self.ranks[root2]:
          self.roots[root1] = root2
        else:
          self.roots[root2] = root1
          self.ranks[root1] += 1
        return False  # we can't remove this edge because it's used
      else:
        return True  # we can remove this edge because there already is a path for these 2 nodes.
    
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
      \"\"\"
      Union find for alice and bob separately. But the trick here is that we must go over type 3 first, because
      once we have type 3, then for the same node pair, we don't ever need type1 or type 2. But if we see types 
      in such order: 1, 3, 2. We can remove type 1, but we can't remove type2, because at that point type 1 is
      already removed.
      Time:
      So we need to sort the edges by type first: O(eloge), then iterate over the edges O(e)
      In fact, we can remove the sort if we loop over the edges twice, the first time we only do type 3, and
      then the second type we do the other 2 types. This removes the sorting complexity.
      \"\"\"
      # with sorting:
#       edges.sort(key=lambda edge: -edge[0])  
#       removes = 0
#       self.groups = n * 2
#       for tp, n1, n2 in edges:
#         can_remove = False
#         if tp == 1:
#           can_remove = self.union((1, n1), (1, n2))
#         elif tp == 2:
#           can_remove = self.union((2, n1), (2, n2))
#         else:
#           can_remove1, can_remove2 = self.union((1, n1), (1, n2)), self.union((2, n1), (2, n2))
#           can_remove = can_remove1 and can_remove2
#         removes += (1 if can_remove else 0)  
      
#       # If in the end both alice and alice have a single group, then return removed count
#       return removes if self.groups == 2 else -1 
      
      # without sorting:
      removes = 0
      self.groups = n * 2
      for tp, n1, n2 in edges:  # first iteration
        if tp == 3:
          can_remove1, can_remove2 = self.union((1, n1), (1, n2)), self.union((2, n1), (2, n2))
          removes += (1 if can_remove1 and can_remove2 else 0)  
      
      for tp, n1, n2 in edges:
        can_remove = False
        if tp == 1:
          can_remove = self.union((1, n1), (1, n2))
        elif tp == 2:
          can_remove = self.union((2, n1), (2, n2))
        removes += (1 if can_remove else 0)
      
      return removes if self.groups == 2 else -1 
