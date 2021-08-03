\"\"\"
    1. Problem Summary / Clarifications / TDD:

\"\"\"

class Solution:
    def __init__(self):
        self.moves = [(0,-1),(-1,0),(0,+1),(+1,0)]
        
    def shortestBridge(self, A: List[List[int]]) -> int:
                
        # Find the source islands
        r, c = 0, 0
        while r < len(A) and not A[r][c]:
            while c < len(A[0]) and not A[r][c]:
                c += 1
            c = 0 if c == len(A[0]) else c
            r = r if A[r][c] else r + 1
            
        source = set()
        self.explore_island_dfs(A, r, c, source)
        
        # 2. Find min distance between island 1 and 2: BFS
        visited = source
        curr_level = list(source)
        
        distance = 0
        while curr_level:
            
            next_level = []
            for (r, c) in curr_level:
                
                for mr, mc in self.moves:
                    ar, ac = r + mr, c + mc
                    
                    if not self.valid_position(A, ar, ac):
                        continue 

                    elif A[ar][ac] and (ar, ac) not in source:
                        return distance
                    
                    elif (ar, ac) not in visited and A[ar][ac] == 0:
                        next_level.append((ar, ac))
                        visited.add((ar, ac))
            
            distance += 1
            curr_level = next_level
                    
        return -1
        
    def explore_island_dfs(self, A: List[List[int]], r, c, visited):
                
        visited.add((r, c))
        for mr, mc in self.moves:
            ar, ac = r + mr, c + mc
            if self.valid_position(A, ar, ac) and (ar, ac) not in visited and A[ar][ac]:
                self.explore_island_dfs(A, ar, ac, visited)
    
    def valid_position(self, A, r, c):
        
        if r in (-1, len(A)) or c in (-1, len(A[0])):
            return False
        
        else:
            return True
        
        
                    
                
        
