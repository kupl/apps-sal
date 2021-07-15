# from collections import deque
# class Solution:
#     def shortestPath(self, grid: List[List[int]], k: int) -> int:
#         if len(grid) == 1 and len(grid[0]) == 1:
#             return 0

#         queue = deque([(0,0,k,0)])
#         visited = set([(0,0,k)])

#         if k > (len(grid)-1 + len(grid[0])-1):
#             return len(grid)-1 + len(grid[0])-1

#         while queue:
#             row, col, eliminate, steps = queue.popleft()
#             for new_row, new_col in [(row-1,col), (row,col+1), (row+1, col), (row, col-1)]:
#                 if (new_row >= 0 and
#                     new_row < len(grid) and
#                     new_col >= 0 and
#                     new_col < len(grid[0])):
#                     if grid[new_row][new_col] == 1 and eliminate > 0 and (new_row, new_col, eliminate-1) not in visited:
#                         visited.add((new_row, new_col, eliminate-1))
#                         queue.append((new_row, new_col, eliminate-1, steps+1))
#                     if grid[new_row][new_col] == 0 and (new_row, new_col, eliminate) not in visited:
#                         if new_row == len(grid)-1 and new_col == len(grid[0])-1:
#                             return steps+1
#                         visited.add((new_row, new_col, eliminate))
#                         queue.append((new_row, new_col, eliminate, steps+1))

#         return -1
from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        queue = deque([(0,0,k,0)])
        rows = len(grid)
        cols = len(grid[0])
        ans = float('inf')
        vis = {(0,0,k): 1}
        while len(queue) > 0:
            # print(queue)
            x, y, rem, depth = queue.popleft()
            # print(x,y,rem,depth)
            if x == rows - 1 and y == cols - 1:
                return depth
            for i, j in [[1,0], [0,1], [-1,0], [0,-1]]:
                i += x
                j += y
                if i < 0 or i >= rows or j < 0 or j >= cols or (i,j, rem) in vis or (grid[i][j] == 1 and rem <= 0):
                    continue
                elif grid[i][j] == 0 and (i,j,rem) not in vis:
                    vis[(i,j,rem)] = 1
                    queue.append((i,j,rem,depth+1))
                elif grid[i][j] == 1 and rem > 0 and (i,j, rem-1) not in vis:
                    vis[(i,j,rem-1)] = 1
                    queue.append((i,j,rem-1,depth+1))
        if ans == float('inf'):
            return -1
        return ans
