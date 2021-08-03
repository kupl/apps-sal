def avoid_obstacles(arr):
    s = set(arr)
    m = max(arr)
    for i in range(1, m + 2):
        if i in s:
            continue
        if not any(x in s for x in range(i, m + 1, i)):
            return i
