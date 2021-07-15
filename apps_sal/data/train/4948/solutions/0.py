def resistor_parallel(*rs):
    return 1 / sum(1.0 / r for r in rs)
