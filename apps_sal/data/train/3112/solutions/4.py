def avoid_obstacles(arr, n=1):
    arr = set(arr)
    while set(range(0, 100+1, n)) & arr:
        n += 1
    return n
