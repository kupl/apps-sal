def index(array, n):
    x=len(array)
    if n > x - 1:
        return -1
    else:
        return array[n] ** n
