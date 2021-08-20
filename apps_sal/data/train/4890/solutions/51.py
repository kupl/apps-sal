def find_difference(a, b):
    x = 1
    y = 1
    for i in range(len(a)):
        x = x * a[i]
    for j in range(len(b)):
        y = y * b[j]
    if x >= y:
        return x - y
    else:
        return y - x
