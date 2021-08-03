def find_difference(a, b):
    if ((a[0] * a[1] * a[2]) - (b[0] * b[1] * b[2])) >= 0:
        return ((a[0] * a[1] * a[2]) - (b[0] * b[1] * b[2]))
    elif ((b[0] * b[1] * b[2]) - (a[0] * a[1] * a[2])) >= 0:
        return (b[0] * b[1] * b[2]) - (a[0] * a[1] * a[2])
