move = lambda (r, c), maze: [(rr, cc) for rr, cc in [(r,c-1),(r,c+1),(r-1,c),(r+1,c)] if maze[rr][cc] != '#']
done = lambda where, maze: any(r * c == 0 or r == len(maze) - 1 or c == len(maze[0]) - 1 for r, c in where)

def has_exit(maze):  
    where, seen = set([(r, c) for r in range(len(maze)) for c in range(len(maze[0])) if maze[r][c] == 'k']), set()
    if len(where) != 1: raise ValueError('Wrong number of Kates')
    
    while where and not done(where, maze):
        seen |= where
        where = set([p for  a in [move(p, maze) for p in where] for p in a]) - seen
    
    return done(where, maze)
