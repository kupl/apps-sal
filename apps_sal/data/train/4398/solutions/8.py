def elevator_distance(ls):
    return sum(abs(x - y) for x, y in zip(ls, ls[1:]))
