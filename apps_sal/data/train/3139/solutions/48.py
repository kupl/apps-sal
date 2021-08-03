def index(array, n):
    try:
        x = array[n]
    except IndexError:
        return -1
    y = x**n
    return y
