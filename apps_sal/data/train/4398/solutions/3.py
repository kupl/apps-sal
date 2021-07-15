def elevator_distance(array):
    return sum(abs(a - b) for a, b in zip(array, array[1::]))
