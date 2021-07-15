D = {(0,1):{(-1,0):'L', (1,0):'R', (0,-1):'B'}, (1,0):{(0,1):'L', (0,-1):'R', (-1,0):'B'},
     (0,-1):{(1,0):'L', (-1,0):'R', (0,1):'B'}, (-1,0):{(0,-1):'L', (0,1):'R', (1,0):'B'}}
     
def escape(maze):
    P = {(r, c) for r, row in enumerate(maze) for c, v in enumerate(row) if v == ' '}
    
    paths = [[{(r, c) for r, row in enumerate(maze) for c, v in enumerate(row) if v in '<>^v'}.pop()]]
    faces = {'v':(1, 0), '^':(-1,0), '<':(0,-1), '>':(0, 1)}[{c for r in maze for c in r if c in '<>^v'}.pop()]
    
    while paths:
        newp = []
        for path in paths:
            r, c = path[-1]
                
            # Have we escaped?
            if r * c == 0 or r == len(maze) - 1 or c == len(maze[0]) - 1:                
                moves = []
                for p in [(b[0] - a[0], b[1] - a[1]) for a, b in zip(path, path[1:])]:
                    moves += ([D[faces][p]] if faces != p else []) + ['F']
                    faces = p
                return moves
                
            # Are there any more moves to be made on this path?
            for p in {(r+1, c), (r-1, c), (r, c+1), (r, c-1)} & P:
                newp.append(path + [p])
                P.remove(p)
        paths = newp
    return []
