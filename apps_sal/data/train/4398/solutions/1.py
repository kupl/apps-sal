def elevator_distance(array):
    return sum(abs(array[i + 1] - array[i]) for i in range(len(array) - 1))
