class Solution:
    class Tup:
        def __init__(self, u, l):
            self.u = u
            self.l = l
        def __str__(self):
            return f\"({self.u}, {self.l})\"
    
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        yl = len(grid)
        xl = len(grid[0])
        mem = []
        for y in range(0, yl):
            for x in range(0, xl):
                if x == 0:
                    mem.append([])
                row = mem[y]
                if grid[y][x] == 0:
                    row.append((0,0))
                    continue
                u = grid[y][x] if y == 0 else mem[y - 1][x][0] + 1
                l = grid[y][x] if x == 0 else mem[y][x - 1][1] + 1
                row.append((u, l))
        ml = 0
        print(mem)
        for y in range(0, yl):
            for x in range(0, xl):
                for l in range(0, min(mem[y][x])):
                    if mem[y - l][x][1] >= l + 1 and mem[y][x - l][0] >= l + 1:
                        ml = max(ml, l + 1)
        return ml * ml
                
        
