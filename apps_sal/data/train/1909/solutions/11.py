class Solution:
    import copy
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0]) if ROWS else 0
        
        right = copy.deepcopy(grid)
        down = copy.deepcopy(grid)
        for r in reversed(range(ROWS)):
            for c in reversed(range(COLS-1)):
                if right[r][c]:
                    right[r][c] += right[r][c+1]
                    
        for r in reversed(range(ROWS-1)):
            for c in reversed(range(COLS)):
                if down[r][c]:
                    down[r][c] += down[r+1][c]
        
        # print(grid)
        # print(down)
        # print(right)
        
        RET = 0
        for r in range(ROWS):
            for c in range(COLS):
                CAP = min(right[r][c], down[r][c])
                for shift in reversed(range(RET, CAP)):
                    if right[r+shift][c] > shift and down[r][c+shift] > shift:
                        RET = shift+1
                        break
        return RET**2
