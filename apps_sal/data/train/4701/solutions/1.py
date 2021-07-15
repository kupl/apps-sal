from math import ceil

def pay_cheese(lst):
    return f"L{35 * ceil(sum(lst) / 100)}"
