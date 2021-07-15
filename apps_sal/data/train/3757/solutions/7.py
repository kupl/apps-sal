from math import floor, ceil

def rond(x):
    return floor(x) if x % 1 < 0.5 else ceil(x)
    
def round_to_five(numbers):
    return [rond(x/5)*5 for x in numbers]
