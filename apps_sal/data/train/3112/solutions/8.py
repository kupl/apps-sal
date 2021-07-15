def avoid_obstacles(arr):
    holes = set(range(2, max(arr))).difference(arr)
    for step in holes:
        if all([x % step != 0 for x in arr]):
            return step
    return max(arr) + 1
