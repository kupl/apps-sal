class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def getOr(x1, y1, x2, y2): return 'H' if y2 == y1 + 1 else 'V'
        def inB(x, y): return x < rows and x >= 0 and y < cols and y >= 0
        dic = {(rows - 1, cols - 2, rows - 1, cols - 1): 0}

        def dfs(x1, y1, x2, y2, visited):
            mn = float('inf')
            visited.add((x1, y1, x2, y2))
            if (x1 == rows - 1 and y1 == cols - 2 and x2 == rows - 1 and y2 == cols - 1):
                return 0
            x, y = x1, y1
            if getOr(x1, y1, x2, y2) == 'H':
                r1, c1, r2, c2 = x, y + 1, x, y + 2
                if(r1, c1, r2, c2) in dic:
                    mn = min(mn, 1 + dic[(r1, c1, r2, c2)])
                elif inB(r1, c1) and inB(r2, c2) and grid[r2][c2] == 0 and (r1, c1, r2, c2) not in visited:
                    mn = min(mn, 1 + dfs(r1, c1, r2, c2, visited))
                r1, c1, r2, c2 = x + 1, y, x + 1, y + 1
                if(r1, c1, r2, c2) in dic:
                    mn = min(mn, 1 + dic[(r1, c1, r2, c2)])
                elif inB(r1, c1) and inB(r2, c2) and grid[r1][c1] == 0 and grid[r2][c2] == 0 and (r1, c1, r2, c2) not in visited:
                    mn = min(mn, 1 + dfs(r1, c1, r2, c2, visited))
                r1, c1, r2, c2 = x, y, x + 1, y
                if(r1, c1, r2, c2) in dic:
                    mn = min(mn, 1 + dic[(r1, c1, r2, c2)])
                elif inB(r1, c1) and inB(r2, c2) and grid[r2][c2] == 0 and grid[r2][c2 + 1] == 0 and (r1, c1, r2, c2) not in visited:
                    mn = min(mn, 1 + dfs(r1, c1, r2, c2, visited))
            else:
                r1, c1, r2, c2 = x + 1, y, x + 2, y
                if(r1, c1, r2, c2) in dic:
                    mn = min(mn, 1 + dic[(r1, c1, r2, c2)])
                elif inB(r1, c1) and inB(r2, c2) and grid[r2][c2] == 0 and (r1, c1, r2, c2) not in visited:
                    mn = min(mn, 1 + dfs(r1, c1, r2, c2, visited))
                r1, c1, r2, c2 = x, y + 1, x + 1, y + 1
                if(r1, c1, r2, c2) in dic:
                    mn = min(mn, 1 + dic[(r1, c1, r2, c2)])
                elif inB(r1, c1) and inB(r2, c2) and grid[r1][c1] == 0 and grid[r2][c2] == 0 and (r1, c1, r2, c2) not in visited:
                    mn = min(mn, 1 + dfs(r1, c1, r2, c2, visited))
                r1, c1, r2, c2 = x, y, x, y + 1
                if(r1, c1, r2, c2) in dic:
                    mn = min(mn, 1 + dic[(r1, c1, r2, c2)])
                elif inB(r1, c1) and inB(r2, c2) and grid[r2 + 1][c2] == 0 and grid[r2][c2] == 0 and (r1, c1, r2, c2) not in visited:
                    mn = min(mn, 1 + dfs(r1, c1, r2, c2, visited))
            dic[(x1, y1, x2, y2)] = mn
            return mn

        d = dfs(0, 0, 0, 1, set())
        return d if d != float('inf') else -1
