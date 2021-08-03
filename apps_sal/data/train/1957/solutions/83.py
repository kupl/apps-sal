from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        q = deque([(0, 0, 0, k)])
        visited = set([(0, 0, k)])
        if len(grid[0]) == 1 and len(grid) == 1:
            return 0
        while q:
            row, col, dist, cur_k = q.popleft()
            for nr, nc in [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]:
                d = dist + 1
                if nr < len(grid) and nr >= 0 and nc < len(grid[0]) and nc >= 0:
                    if (nr, nc, cur_k) not in visited and grid[nr][nc] == 0:
                        if nr == len(grid) - 1 and nc == len(grid[0]) - 1:
                            return dist + 1
                        q.append((nr, nc, d, cur_k))
                        visited.add((nr, nc, cur_k))
                    if (nr, nc, cur_k - 1) not in visited and grid[nr][nc] == 1:
                        if cur_k > 0:
                            if nr == len(grid) - 1 and nc == len(grid[0]) - 1:
                                return dist + 1
                            q.append((nr, nc, d, cur_k - 1))
                            visited.add((nr, nc, cur_k - 1))
        return -1

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
