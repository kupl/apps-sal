import math
def halving_sum(n):
    ne = 1
    while n > 1:
        ne += n
        n = n/2
        n = math.floor(n)
    return ne
