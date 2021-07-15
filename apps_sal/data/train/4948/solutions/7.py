def resistor_parallel(*resistors):
    return 1.0 / sum(map(lambda x:1.0/x, resistors))
