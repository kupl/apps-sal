from collections import deque

class Solution:
  def frogPosition(self, n: int, edges_inp: List[List[int]], t: int, target: int) -> float:
    edges = [ [] for _ in range(n+1) ]
    for v0, v1 in edges_inp:
      edges[v0].append( v1 )
      edges[v1].append( v0 )
    # determine at what step and what probability 
    visited = [0 for _ in range(n+1)]
    q = deque()   # format (vertice, step, probability)
    visited[1] = 1
    q.append( (1,0,1.0) )
    print(edges)
    while q:
      node, step, prob = q.popleft()
      print(node, step, prob)
      if step>t:
        return 0
      sub = 0 if node==1 else 1
      if node == target:
        if step == t or len(edges[node]) == sub:
          return prob
      if len(edges[node]) > sub:
        prob_next = prob / (len(edges[node])-sub)
        for node_next in edges[node]:
          if visited[node_next]:
            continue
          print(\">\", node, node_next, step+1, prob_next)
          q.append( (node_next, step+1, prob_next) )
          visited[node_next] = 1
    return 0
  
