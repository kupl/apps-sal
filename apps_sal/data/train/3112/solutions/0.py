def avoid_obstacles(arr):
    n = 2
    while 1:
        if all([x % n for x in arr]):
            return n
        n += 1
