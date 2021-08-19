class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        r, c = len(grid), len(grid[0])
        qu = deque([[0, 0, 0, 0]])
        visited = set()
        while qu:
            i, j, cnt, length = qu.popleft()
            visited.add((i, j, cnt))
            if (i, j) == (r - 1, c - 1):
                return length
            for x, y in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                if 0 <= x < r and 0 <= y < c:
                    new_cnt = cnt if grid[x][y] == 0 else cnt + 1
                    if new_cnt <= k and (x, y, new_cnt) not in visited:
                        visited.add((x, y, new_cnt))
                        qu.append([x, y, new_cnt, length + 1])
        return -1


# class Solution:
#     def shortestPath(self, grid: List[List[int]], k: int) -> int:
#         if len(grid) == 1 and len(grid[0]) == 1:
#             return 0

#         q = collections.deque([(0, 0, 0, 0)])
#         m, n = len(grid), len(grid[0])
#         visited = set()

#         while q:
#             x, y, obstacle, path = q.popleft()
#             for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
#                 if 0 <= i < m and 0 <= j < n:
#                     if grid[i][j] == 1 and obstacle < k and (i, j, obstacle + 1) not in visited:
#                         visited.add((i, j, obstacle + 1))
#                         q.append((i, j, obstacle + 1, path + 1))
#                     if grid[i][j] == 0 and (i, j, obstacle) not in visited:
#                         if (i, j) == (m - 1, n - 1):
#                             return path + 1
#                         visited.add((i, j, obstacle))
#                         q.append((i, j, obstacle, path + 1))

        return -1
