def resistor_parallel(*xs):
    return 1 / sum((1 / x for x in map(float, xs)))
