from itertools import combinations

def digits(num):
    return [sum(pair) for pair in combinations([int(d) for d in str(num)], 2)]

