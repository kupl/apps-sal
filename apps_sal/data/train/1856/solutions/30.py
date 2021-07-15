class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if not grid[n - 1][n - 2] == grid[n - 1][n - 1] == 0:
            return -1
        
        locs = set([(0, 0, 'h'), ]) #(i, j, alignment, just rotated)
        visited = set(locs)
        time = 0
        while locs and (n-1, n-2, 'h') not in locs and (n-1, n-2, 'h') not in locs:
            time += 1
            new_locs = set()
            for i, j, align in locs:
                # move right
                if align == 'h' and j + 2 < n and (i, j+1, 'h') not in visited and not grid[i][j+2]:
                    new_locs.add((i, j + 1, 'h'))
                if align == 'v' and j + 1 < n and (i, j+1, 'v') not in visited and not grid[i][j+1] and not grid[i+1][j+1]:
                    new_locs.add((i, j + 1, 'v'))
                # move down
                if align == 'h' and i + 1 < n and (i+1, j, 'h') not in visited and not grid[i+1][j] and not grid[i+1][j+1]:
                    new_locs.add((i+1, j, 'h'))
                if align == 'v' and i + 2 < n and (i+1, j, 'v') not in visited and not grid[i+2][j]:
                    new_locs.add((i+1, j, 'v'))
                # hor -> vert
                if align == 'h' and i + 1 < n and (i, j, 'v') not in visited and not grid[i+1][j] and not grid[i+1][j+1]:
                    new_locs.add((i, j, 'v'))
                # vert -> hor
                if align == 'v' and j + 1 < n and (i, j, 'h') not in visited and not grid[i][j+1] and not grid[i+1][j+1]:
                    new_locs.add((i, j, 'h'))
            locs = set(new_locs)
            visited |= locs
            
        if (n-1, n-2, 'h') in locs or (n-1, n-2, 'h') in locs:
            return time
        
        else:
            return -1

