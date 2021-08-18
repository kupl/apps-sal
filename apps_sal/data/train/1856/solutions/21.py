class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        vis = set()
        q = collections.deque([(0, 0, 0, 0)])
        d = [[0, 1], [1, 0]]
        n = len(grid)
        while q:
            node = q.popleft()
            if node[0] == (n - 1) and node[1] == (n - 2) and node[2] == 0:
                return node[3]
            snake = [[node[0], node[1]], [node[0] + d[node[2]][0], node[1] + d[node[2]][1]]]
            for i in d:
                possible = True
                for c in snake:
                    nx = c[0] + i[0]
                    ny = c[1] + i[1]
                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        possible = False
                        break
                    if grid[nx][ny] != 0:
                        possible = False
                        break
                if possible:
                    nx = node[0] + i[0]
                    ny = node[1] + i[1]
                    if (nx, ny, node[2]) not in vis:
                        vis.add((nx, ny, node[2]))
                        q.append((nx, ny, node[2], node[3] + 1))
                    if node[2] == 0 and i[0] == 1:
                        if (node[0], node[1], 1) not in vis:
                            vis.add((node[0], node[1], 1))
                            q.append((node[0], node[1], 1, node[3] + 1))
                    elif node[2] == 1 and i[0] == 0:
                        if (node[0], node[1], 0) not in vis:
                            vis.add((node[0], node[1], 0))
                            q.append((node[0], node[1], 0, node[3] + 1))
        return -1
