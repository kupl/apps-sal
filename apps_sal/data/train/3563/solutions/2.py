import math

def distance(n) :
    if n == 1: return 0
    level = (math.ceil(n**0.5) // 2)
    l_start = ((level * 2) - 1)**2 + 1
    quad = (n - l_start) // (2 * level)
    l_span = (2 * level) + 1
    direct = (l_start - 1 + (l_span // 2)) + (l_span - 1) * quad
    dist = (level) + abs(direct - n)
    return dist
