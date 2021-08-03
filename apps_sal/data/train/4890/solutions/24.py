def find_difference(a, b):
    x = a[0] * a[1] * a[2]
    y = b[0] * b[1] * b[2]
    z = x - y
    if z > 0:
        return z
    else:
        return -z
    # Your code here!
