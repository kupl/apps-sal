from math import ceil


def cost(mins):
    periods = ceil((mins - 5) / 30)
    return 30 if periods <= 2 else 30 + (periods - 2) * 10
