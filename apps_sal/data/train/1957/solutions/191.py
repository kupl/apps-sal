from collections import deque


def bfs(a, k):
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    if a[0][0] == 1 and k == 0:
        return -1
    q = deque()
    q.append(((0, 0), k - a[0][0], 0))
    visited = set()
    while q:
        item, k, dist = q.popleft()
        if (item, k) in visited:
            continue
        if item == (len(a) - 1, len(a[0]) - 1):
            return dist
        visited.add((item, k))
        for dir in dirs:
            x = item[0] + dir[0]
            y = item[1] + dir[1]
            if 0 <= x < len(a) and 0 <= y < len(a[0]):
                if a[x][y] == 0:
                    q.append(((x, y), k, dist + 1))
                else:
                    if k > 0:
                        q.append(((x, y), k - 1, dist + 1))
    return -1


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        return bfs(grid, k)
