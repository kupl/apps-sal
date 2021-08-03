def index(array, n):
    y = 0
    if n > len(array) - 1:
        y = -1
    else:
        y = pow(array[n], n)
    return y
