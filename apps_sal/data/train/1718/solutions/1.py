def has_exit(maze):
    W = len(maze[0])                                                    # W = width of the maze
    S = W * len(maze)                                                   # S = total cells in the maze
    frontier, unseen = set(), set()                                     # Declaring sets that we'll use for BFS
    for position, content in enumerate("".join(maze)):                  # Use 1D representation for unique address of each cell
        (frontier.add, unseen.add, id)["k #".index(content)](position)  # Populate our sets: put Kate into frontier, passages into unseen
    assert len(frontier) == 1                                           # Check for one and only one Kate
    while frontier:                                                     # Do we still have any options to move further?
        position = frontier.pop()                                       # Take out one of the options
        if min(position, S - position) < W or -~position % W < 2:       # Is it on the edge?
            return True                                                 # If so, we found an exit! Hurray!
        for way in (position - W,                                       # Look up
                    position + W,                                       # Look down
                    position - 1,                                       # Look left
                    position + 1):                                      # Look right
            if way in unseen:                                           # If there is no wall, there is a way
                frontier.add (way)                                      # Let's add this to our options
                unseen.remove(way)                                      # We've seen it already
    return False                                                        # We are out of options. So saaaad :(
