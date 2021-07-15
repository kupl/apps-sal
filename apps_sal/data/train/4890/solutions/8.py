def find_difference(a, b):
    return abs(p(a) - p(b))
    
def p(a):
    temp = 1
    for i in a:
        temp *= i
    return temp
