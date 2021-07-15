def path_finder(maze):
    g = maze.splitlines()
    end, bag = len(g[0]) -1 + len(g) * 1j - 1j, {0}
    grid = {x + y * 1j for y,l in enumerate(g) for x,c in enumerate(l) if '.' == c}
    while bag:
        if end in bag: return True
        grid -= bag
        bag = grid & set.union(*({z + 1j ** k for k in range(4)} for z in bag))
    return False
