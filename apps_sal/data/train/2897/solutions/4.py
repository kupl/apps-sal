import math
def oddity(n):
    if int(math.sqrt(n))**2 == n:
        return 'odd'
    return 'even'
