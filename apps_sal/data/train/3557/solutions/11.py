import math
def odd_count(n):
    if n % 2 != 0:
        return (n-1)/2
    else:
        return math.ceil((n-1)/2)

