import collections
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        self.g = grid
        visited = set()
        visited.add((0,0,0))
        
        q = collections.deque()
        q.append((0,0,0,0))
        
        target = (len(grid)-1, len(grid[0])-1)
        
        while q:
            node = q.popleft()
            
            if (node[0], node[1]) == target:
                return node[3]
            
            for n in self.neigh(node):
                nk = node[2] + (1 if grid[n[0]][n[1]] == 1 else 0)
                if (n[0], n[1], nk) not in visited and nk <= k:
                    visited.add((n[0], n[1], nk))
                    q.append((n[0], n[1], nk, node[3]+1))
        
        return -1
                
        
        
    def neigh(self, pos):
        cand = [
            (pos[0]+1, pos[1]),
            (pos[0]-1, pos[1]),
            (pos[0], pos[1]+1),
            (pos[0], pos[1]-1)
        ]
        
        out = []
        
        for c in cand:
            if c[0] >= 0  and c[0] < len(self.g) and c[1] >= 0 and c[1] < len(self.g[0]):
                out.append(c)
        
        return out
    
    

