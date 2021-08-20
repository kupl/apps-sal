def index(array, n):
    if n >= len(array):
        return -1
    else:
        return array[n] ** n
