def elevator_distance(floors):
    return sum(abs(floors[i + 1] - floors[i]) for i in range(len(floors) - 1))
