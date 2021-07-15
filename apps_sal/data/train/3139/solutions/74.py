def index(array, n):
    try:
        x = array.pop(n)
    except IndexError:
        return -1
    return x**n
