def avoid_obstacles(arr):
    x = 2
    for i in range(max(arr)):
        leaps = [x * i for i in range(1, max(arr))]
        for i in leaps:
            if i in arr:
                leaps = []
                x += 1
                break
    return x
