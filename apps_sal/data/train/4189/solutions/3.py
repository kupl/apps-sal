def worth(s):
    return sum(map(ord, s))
    
def highest_value(a, b):
    return max(a, b, key=worth)
