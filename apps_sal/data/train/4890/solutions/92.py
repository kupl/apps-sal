def prod(arr):
    result = 1
    for i in arr:
        result *= i
    return result

def find_difference(a, b):
    return abs(prod(a) - prod(b))
