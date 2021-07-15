import math
def oddity(n):
    return math.sqrt(n) % 1 == 0 and 'odd' or 'even'
