def find_difference(a, b):
    x = y = 1
    for i in a:
        x *= i
    for j in b:
        y *= j
    return abs(x-y)
