class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = collections.deque()
        v = {}
        q.append((0, 0, k, 0))  # x, y , k and step

        while q:
            x, y, z, s = q.popleft()
            v[(x,y)] = z
            if x == (m - 1) and y == (n - 1):
                return s
            for dx, dy in d:
                nx , ny = x+dx, y+dy
                if nx >= 0 and nx < m and ny >= 0 and ny < n and ((
                nx,ny) not in v or v[(nx,ny)]<z-grid[nx][ny]):
                    if nx == m - 1 and ny == n - 1:
                        return s + 1
                    if (grid[nx][ny] == 1 and z > 0):
                        q.append((nx, ny , z - 1, s + 1))
                        v[(nx ,ny)]=z-1
                    elif grid[nx][ny] == 0:
                        q.append((nx, ny, z, s + 1))
                        v[(nx ,ny )] = z
                    else:
                        continue

        return -1
