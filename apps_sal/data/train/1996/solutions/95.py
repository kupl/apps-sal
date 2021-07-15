class Solution:
  def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
    cycle_nodes = set()
    safe_nodes = set()
    visited = set()
    
    def helper(node: int, visited: set) -> bool:
      if node in cycle_nodes:
        return False
      if node in safe_nodes:
        return True
      
      if node in visited:
        cycle_nodes.add(node)
        return False
      
      visited.add(node)
      
      for child in graph[node]:
        if helper(child, visited) is False:
          cycle_nodes.add(node)
          return False
      
      safe_nodes.add(node)
      return True
    
    ans = []
    for node in range(len(graph)):
      if helper(node, visited):
        ans.append(node)
    
    return ans
    
        
        
    
    
    # (0), (1, 2)
    # (0, 1), (2, 2, 3)
    # (0, 1, 2), (2, 3, 5)
    # ()

