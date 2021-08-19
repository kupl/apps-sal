def resistor_parallel(*args):
    return 1 / sum((1.0 / a for a in args))
