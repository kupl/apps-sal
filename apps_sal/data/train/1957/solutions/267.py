from collections import deque
class Solution:
    
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        num_rows = len(grid)   
        num_cols = len(grid[0])
        
        frontier = deque([(0, 0, 0, k)]) # frontier keeps (row, col, dist, k)
        visited = {}
        
        while frontier:
                row, col, dist, chances = frontier.popleft()
                if chances < 0:
                    continue
                if row == num_rows - 1 and col == num_cols - 1:
                    return dist
                
                #get neighbours
                neighbours = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
                
                for neighbour in neighbours:
                    if self.valid_neighbour(neighbour, grid):
                        neigh_row = neighbour[0]
                        neigh_col = neighbour[1]
                        if neighbour not in visited:
                            if grid[neigh_row][neigh_col] == 0:
                                frontier.append((neigh_row, neigh_col, dist + 1, chances))
                                visited[neighbour] = (dist + 1, chances)
                            else:
                                frontier.append((neigh_row, neigh_col, dist + 1, chances - 1))
                                visited[neighbour] = (dist + 1, chances - 1)
                        else: # if visited, only visit again if chance is larger
                            last_dist, last_chance = visited[neighbour]
                            if last_chance < chances:
                                if grid[neigh_row][neigh_col] == 0:
                                    frontier.append((neigh_row, neigh_col, dist + 1, chances))
                                    visited[neighbour] = (dist + 1, chances)
                                else:
                                    frontier.append((neigh_row, neigh_col, dist + 1, chances - 1))
                                    visited[neighbour] = (dist + 1, chances - 1)
                                
                            
        return -1
    
    def valid_neighbour(self, neighbour, grid):
        row = neighbour[0]
        col = neighbour[1]
        
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]):
            return False
        return True
        

