class Solution:
    def bfs(self, M: List[List[List[int]]]) -> int:
        Q = deque()
        visited = set()
        Q.append((0, 0, 0, 0))
        visited.add((0, 0, 0))
        while(len(Q) != 0):
            k, i, j, depth = Q.popleft()
            if(depth > 25):
                print(k, i, j, depth)
            if((k, i, j) == (0, self.m - 1, self.n - 2)):
                return depth
            if(j + 1 < len(M[k][i]) and (k, i, j + 1) not in visited and M[k][i][j + 1] == 0):
                Q.append((k, i, j + 1, depth + 1))
                visited.add((k, i, j + 1))
            if(i + 1 < len(M[k]) and (k, i + 1, j) not in visited and M[k][i + 1][j] == 0):
                Q.append((k, i + 1, j, depth + 1))
                visited.add((k, i + 1, j))
            if(i + 1 < self.n and j + 1 < self.m and (k ^ 1, i, j) not in visited and M[2][i][j] == 0):
                Q.append((k ^ 1, i, j, depth + 1))
                visited.add((k ^ 1, i, j))
        return -1

    def minimumMoves(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        M = [[[0] * (self.n - 1) for i in range(self.m)], [[0] * (self.n) for i in range(self.m - 1)], [[0] * (self.n - 1) for i in range(self.m - 1)]]
        for i in range(self.m):
            for j in range(self.n):
                if(j + 1 < self.n):
                    M[0][i][j] = (grid[i][j] | grid[i][j + 1])
                if(i + 1 < self.m):
                    M[1][i][j] = (grid[i][j] | grid[i + 1][j])
                if(i + 1 < self.m and j + 1 < self.n):
                    M[2][i][j] = (grid[i][j] | grid[i + 1][j] | grid[i][j + 1] | grid[i + 1][j + 1])
        return self.bfs(M)
