from itertools import count, takewhile

def halving_sum(n): 
    g = (2**j for j in count(0))
    g = takewhile(lambda x: n >= x, g)
    return sum(n // i for i in g)

