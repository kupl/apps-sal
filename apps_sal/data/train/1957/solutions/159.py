class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        seen = set()
        seen.add((0,0,k))
        q = deque([(0,0,k,0)])
                
        while q:
            x,y, remaining, moves = q.popleft()
            
            if x == len(grid)-1 and y == len(grid[0])-1: return moves
            
            for new_x, new_y in [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]:
                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                    if grid[new_x][new_y] == 1 and (new_x,new_y,remaining-1) not in seen and remaining > 0:
                        seen.add((new_x,new_y,remaining-1))
                        q.append((new_x, new_y, remaining-1, moves+1))
                        
                    elif grid[new_x][new_y] == 0 and (new_x,new_y,remaining) not in seen:
                        seen.add((new_x,new_y,remaining))
                        q.append((new_x, new_y, remaining, moves+1))
        
        return -1

