def elevator_distance(array):
    n = len(array)
    m = 0
    total_dist = 0
    while n >= 2:
        distance = abs(array[m] - array[m + 1])
        total_dist += distance
        n -= 1
        m += 1
    return total_dist
