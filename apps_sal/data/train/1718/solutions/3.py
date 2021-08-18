def has_exit(maze):
    vector, w = list("".join(maze)), len(maze[0])
    assert vector.count("k") == 1
    while "k" in vector:
        for p, cell in enumerate(vector):
            if cell == "k":
                if min(p, len(vector) - p) < w or -~p % w < 2:
                    return True
                for direction in (-w, 1, w, -1):
                    if vector[p + direction] == " ":
                        vector[p + direction] = "k"
                vector[p] = "+"
    return False
