def ant(gr, cl, ro, n, di = 0):
    class ant_class():
        def __init__(self, col, row, direction):
            self.c = col
            self.r = row
            self.direction = ['N', 'E', 'S', 'W']
        def __repr__(self):
            return ('col: {}, row: {}, direction: {}'.format(self.c, self.r, self.direction[0]))
        def turn_right(self):
            self.direction.append(self.direction.pop(0))
        def turn_left(self):
            self.direction.insert(0, self.direction.pop(-1))
        def move(self, grid):
            if self.direction[0] == 'N':
                 if ant.r == 0:
                    grid.expand_north()
                 else:
                    ant.r -= 1
            elif self.direction[0] == 'S':
                if ant.r == len(grid.grid) - 1:
                    grid.expand_south()
                ant.r += 1
            elif self.direction[0] == 'W':
                if ant.c == 0:
                    grid.expand_west()
                else:
                    ant.c -= 1
            elif self.direction[0] == 'E':
                if ant.c == len(grid.grid[0]) - 1:
                    grid.expand_east()
                ant.c += 1
    
    class grid():
        def __init__(self, arr):
            self.grid = arr
        def expand_south(self):
            self.grid.append([0 for i in range(len(self.grid[0]))])
        def expand_north(self):
            self.grid.insert(0, [0 for i in range(len(self.grid[0]))])
        def expand_east(self):
            self.grid = [i + [0] for i in self.grid]
        def expand_west(self):
            self.grid = [[0] + i for i in self.grid]
        def invert(self, ant):
            self.grid[ant.r][ant.c] = int(not(self.grid[ant.r][ant.c]))
        
    ant = ant_class(cl, ro, di)
    field = grid(gr)
    for i in range(di):
        ant.turn_right()
    
    for i in range(n):
        if field.grid[ant.r][ant.c] == 1:
            ant.turn_right()
            field.invert(ant)
            ant.move(field)
        elif field.grid[ant.r][ant.c] == 0:
            ant.turn_left()
            field.invert(ant)
            ant.move(field)
    
    return field.grid

