def find_difference(a, b):
    prod1 = 1
    prod2 = 1
    for i in range(3):
        prod1 *= a[i]
        prod2 *= b[i]
    return abs(prod1 - prod2)
