def index(array, n):
    while n >= len(array):
        return -1
    else:
        return array[n] ** n
