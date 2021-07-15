def oneJump( edges, visited, target, cur, t):
    
    if t == 0:
        return 0
    
    if t == 1 and cur == target:
        return 1
    
    nxt = []
    visited[cur] = 1
    
    for i in edges:
        
        if i[0] == cur and visited[i[1]] == 0:
            nxt.append(i[1])
        
        elif i[1] == cur and visited[i[0]] == 0:
            nxt.append(i[0])
    
    if len(nxt) == 0: 
        if cur == target:
            return 1
        else:
            return 0
    
    for i in nxt:
        
        n = oneJump( edges, visited, target, i, t-1)
        if n != 0:
            return (1/len(nxt)) * n
    
    return 0         
    
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        points = [ i for i in range(1,n+1)]
        vis = [0 for i in range(n)]
        
        visited = dict(zip(points, vis))
        return oneJump( edges, visited, target, 1, t+1)
