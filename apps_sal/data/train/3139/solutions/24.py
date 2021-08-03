def index(array, n):
    if n >= len(array) or n < 0:
        return -1
    else:
        return (array[n])**n
