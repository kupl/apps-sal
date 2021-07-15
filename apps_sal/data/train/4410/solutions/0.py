from math import floor, log
def count_sixes(n):
    return floor((n - n % 2) * log(2, 10))
