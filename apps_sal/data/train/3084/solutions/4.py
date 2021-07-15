from collections import Counter

def combine(*args):
    return sum(map(Counter, args), Counter())
