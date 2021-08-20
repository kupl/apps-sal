def index(array, n):
    if n + 1 < len(array):
        return array[n] ** n
    elif n + 1 > len(array):
        return -1
    else:
        return array[n] ** n
