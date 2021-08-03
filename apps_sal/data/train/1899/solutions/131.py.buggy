\"\"\"
    1. Problem Summary / Clarifications / TDD:

\"\"\"

class Solution:
    def __init__(self):
        self.moves = [(0,-1),(-1,0),(0,+1),(+1,0)]
        
    def shortestBridge(self, A: List[List[int]]) -> int:
        
        islands = []
        
        # Find the 2 islands
        visited = set()
        for r in range(len(A)):
            for c in range(len(A[0])):
                if A[r][c] and (r, c) not in visited:
                    island = set()
                    self.explore_island_dfs(A, r, c, visited, island)
                    
                    islands.append(island)
                
        # 2. Find min distance between island 1 and 2
        visited = islands[0]
        curr_level = list(visited)
        
        distance = 0
        while curr_level:
            
            next_level = []
            for (r, c) in curr_level:
                
                for mr, mc in self.moves:
                    ar, ac = r + mr, c + mc
                    
                    if not self.valid_position(A, ar, ac):
                        continue 

                    if (ar, ac) in islands[1]:
                        return distance

                    elif (ar, ac) not in visited and A[ar][ac] == 0:
                        next_level.append((ar, ac))
                        visited.add((ar, ac))
            
            distance += 1
            curr_level = next_level
                    
        return len(A) * len(A[0])
    
    def explore_island_dfs(self, A: List[List[int]], r, c, visited, island):
        
        if r < 0 or r == len(A) or c < 0 or c == len(A[0]) or (r, c) in visited or not A[r][c]:
            return
        
        visited.add((r,c))
        island.add((r,c))
        
        self.explore_island_dfs(A, r - 1, c, visited, island)
        self.explore_island_dfs(A, r, c - 1, visited, island)
        self.explore_island_dfs(A, r + 1, c, visited, island)
        self.explore_island_dfs(A, r, c + 1, visited, island)
    
    def valid_position(self, A, r, c):
        
        if r < 0 or r == len(A) or c < 0 or c == len(A[0]):
            return False
        
        else:
            return True
        
        
                    
                
        
