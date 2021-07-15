def find_difference(a, b): 
    c = (a[0] * a[1] * a[2]) - (b[0] * b[1] * b[2])
    if c < 0:
        return c * (-1)
    else:
        return c

    # Your code here!

