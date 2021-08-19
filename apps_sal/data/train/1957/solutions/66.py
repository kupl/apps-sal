class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        (r, c) = (len(grid), len(grid[0]))
        qu = deque([[0, 0, 0, 0]])
        visited = set()
        while qu:
            (i, j, cnt, length) = qu.popleft()
            visited.add((i, j, cnt))
            if (i, j) == (r - 1, c - 1):
                return length
            for (x, y) in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                if 0 <= x < r and 0 <= y < c:
                    new_cnt = cnt if grid[x][y] == 0 else cnt + 1
                    if new_cnt <= k and (x, y, new_cnt) not in visited:
                        visited.add((x, y, new_cnt))
                        qu.append([x, y, new_cnt, length + 1])
        return -1
        return -1
