def has_exit(maze):
    vector, w = list("".join(maze)), len(maze[0])                # "vector" is 1D representation of the maze; "w" is the width of a maze row
    assert vector.count("k") == 1                                # checking if there is one and only one Kate in the maze
    while "k" in vector:                                         # cycle that pushes Kate clones into previously unvisited adjacent cells
        for p, cell in enumerate(vector):                        # sweeping the maze...
            if cell == "k":                                      # ...for Kate clones
                if min(p, len(vector) - p) < w or -~p % w < 2:   # Kate clone at edge?
                    return True                                  # exit found!
                for direction in (-w, 1, w, -1):                 # otherwise look at adjacent cells
                    if  vector[p + direction] == " ":            # to see if clone can pass through them
                        vector[p + direction]  = "k"             # clone Kate where there is a passage
                vector[p] = "+"                                  # mark cell as visited
    return False                                                 # There is no exit :(

