import math
def odd_count(n):
    return math.ceil((n-1)/2)#len([i for i in range(n) if (i % 2) == 1])
