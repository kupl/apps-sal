import math
def round_up(n, decimals=0): 
    multiplier = 5 ** decimals 
    return math.ceil(n * multiplier) / multiplier

def round_to_next5(n):
    m = round_up(n, -1)
    return m
