class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if not grid:
            return -1
        m, n = len(grid), len(grid[0])
        if grid[0][0] != 0:
            return -1
        if m == 1 and n == 1:
            return 0  # no need to walk
        di = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def get_nei(i, j):
            return [(i + x, j + y) for (x, y) in di if 0 <= i + x <= m - 1 and 0 <= j + y <= n - 1]

        # seen = {(0, 0): 0}
        seen = set([(0, 0, k)])
        # seen2 = {(0, 0): k}
        q = collections.deque()
        q.append((0, 0, k, 0))
        while q:
            i, j, ob, depth = q.popleft()
            for x, y in get_nei(i, j):
                cob = ob
                if x == m - 1 and y == n - 1 and cob >= 0:
                    return depth + 1
                if grid[x][y] == 1 and cob > 0 and (x, y, cob - 1) not in seen:
                    seen.add((x, y, cob - 1))
                    q.append((x, y, cob - 1, depth + 1))
                if grid[x][y] == 0 and cob >= 0 and (x, y, cob) not in seen:
                    seen.add((x, y, cob))
                    q.append((x, y, cob, depth + 1))

                    # cob -= 1
                    # if cob < 0:
                    #     continue
                # if (x, y, cob) in seen:
                #     continue
                # seen.add((x, y, cob))
                # q.append((x, y, cob, depth+1))
        return -1


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
