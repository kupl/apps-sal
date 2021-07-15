from math import ceil

def total_bill(s):
    return 2 * ceil(s.count('r') * 4 / 5)
