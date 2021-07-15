from operator import mul, sub
from functools import reduce

def process_data(data):
    return reduce(mul, [reduce(sub,x) for x in data])
