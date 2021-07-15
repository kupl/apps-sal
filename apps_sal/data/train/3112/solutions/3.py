def avoid_obstacles(arr):
    obstacles = set(arr)
    limit = max(arr) + 2
    for step in range(1, limit):
        if not (set(range(0, limit, step)) & obstacles):
            return step

