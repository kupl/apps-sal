def path_finder(maze):
    lst  = maze.split('\n')
    X, Y = len(lst)-1, len(lst[0])-1
    seen = {(x,y) for x,row in enumerate(lst) for y,c in enumerate(row) if c=='W'} | {(0,0)}
    end, bag, turn = (X,Y), {(0,0)}, 0
    
    while bag and end not in bag:
        bag = { (a,b) for a,b in {(x+dx,y+dy) for x,y in bag for dx,dy in ((0,1), (0,-1), (1,0), (-1,0))}
                      if 0 <= a <= X and 0 <= b <= Y} - seen
        seen |= bag
        turn += 1
    
    return bool(bag) and turn
