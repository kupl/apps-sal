import heapq

def valid(grid, r, c):
    max_r, max_c = len(grid)-1, len(grid[0])-1
    
    if 0 <= r <= max_r and 0 <= c <= max_c and grid[r][c] != \"#\":
        return True
    
    return False

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == \"S\":
                    s_r, s_c = r, c
                if grid[r][c] == \"B\":
                    b_r, b_c = r,c
                if grid[r][c] == \"T\":
                    target = (r,c)
        
        min_queue = [(0, s_r, s_c, b_r, b_c)]
        visited = set()
        directions = ((1,0), (-1, 0), (0,1), (0,-1))
        
        while len(min_queue) > 0:
            cost, s_r, s_c, b_r, b_c = heapq.heappop(min_queue)
            
            if (b_r, b_c) == target:
                return cost
            
            if (s_r, s_c, b_r, b_c) in visited:
                continue
                
            visited.add((s_r, s_c, b_r, b_c))
            
            for dr, dc in directions:
                new_cost = cost
                ns_r, ns_c = s_r + dr, s_c + dc
                nb_r, nb_c = b_r, b_c
                
                if (ns_r, ns_c) == (nb_r, nb_c):
                    new_cost +=1
                    nb_r, nb_c = nb_r + dr, nb_c + dc
                    
                new_state = (ns_r, ns_c, nb_r, nb_c)
                
                if valid(grid, ns_r, ns_c) and valid(grid, nb_r, nb_c) and new_state not in visited:
                    heapq.heappush(min_queue, (new_cost, *new_state))
                
        return -1
                
