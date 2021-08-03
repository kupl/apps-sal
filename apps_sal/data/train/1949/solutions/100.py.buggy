def viable_neighbors(grid, coord):
    y, x = coord
    possible_coords = [
        (y - 1, x),
        (y, x + 1),
        (y + 1, x),
        (y, x - 1),
    ]
    viable_coords = []
    for possible_y, possible_x in possible_coords:
        if 0 <= possible_y < len(grid) and 0 <= possible_x < len(grid[0]) and grid[possible_y][possible_x] != 0:
            viable_coords.append((possible_y, possible_x))
            
    return viable_coords


def dfs(grid, coord, visited, gold):
    visited.add(coord)
    neighbors = viable_neighbors(grid, coord)
    new_gold = gold + grid[coord[0]][coord[1]]
    
    possible_golds = []
    
    for neighbor in neighbors:
        if neighbor not in visited:
            explored_gold = dfs(grid, neighbor, visited, new_gold)
            possible_golds.append(explored_gold)
    
    visited.remove(coord)
    return max(possible_golds or [new_gold])
            
def solve(grid):
    max_gold = 0
    visited = set()
    
    for y, row in enumerate(grid):
        for x, gold_amount in enumerate(row):
            if gold_amount != 0:
                gold_found = dfs(grid, (y, x), visited, 0)
                if gold_found > max_gold:
                    max_gold = gold_found
            
            visited.clear()
            
    return max_gold

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        \"\"\"
        data
        
        grid of m * n size, with integers in it. 0 means the grid should not be traversed
        find the maximum gold possible gained from board if you start from _any_ position of the grid
        
        brute force: iterate through every cell in the grid as a starting point. perform depth first traversal on every neighbor node
        and add up the total gold collected. save the largest collection and return the value.
        
        since each node can only be visited once, we have to explore possibilities, we need to explore every possibility and greedily get the biggest one
        
        
        
        \"\"\"
        return solve(grid)
