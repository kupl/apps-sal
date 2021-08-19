def resistor_parallel(*resistances):
    return 1 / sum((1.0 / r for r in resistances))
