def elevator_distance(array):
    return sum(abs(x-y) for x,y in zip(array[:-1],array[1:]))
