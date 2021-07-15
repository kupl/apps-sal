def abs(x):
    if x<0:
        return -x
    else:
        return x

def norm(x):
    if x == 0:
        return 0
    else:
        return abs(x)//x

def string_to_grid(string):
    return [list(x) for x in string.split('\n')][0:-1]

def grid_to_string(grid):
    result = ''
    for y in range(0,len(grid)):
        result += ''.join(grid[y]) + '\n'
    return result
def connect_two_points(p1,p2,grid):
    ydiff = p2[0] - p1[0]
    xdiff = p2[1] - p1[1]
    ystep = norm(ydiff)
    xstep = norm(xdiff)
    
    step = (ystep,xstep)
    
    for i in range(0,max(abs(ydiff),abs(xdiff))+1):
        y_coord = p1[0] + ystep*i
        x_coord = p1[1] + xstep*i
        
        grid[y_coord][x_coord] = '*'

def generate_point_dictionary(grid):
    D = {}
    for y in range(0,len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] != ' ':
                D[grid[y][x]] = [y,x]
    return D
    
def connect_the_dots(inp):
    grid = string_to_grid(inp)
    D = generate_point_dictionary(grid)
    alph = 'abcdefghijklmnopqrstuvwxyz'
    for x in range(0,len(alph)):
        try:
            connect_two_points(D[alph[x]],D[alph[x+1]],grid)
        except:
            return grid_to_string(grid)
            

