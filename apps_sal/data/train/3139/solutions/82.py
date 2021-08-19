def index(array, n):
    if n <= len(array) - 1:
        n = array[n] ** n
        return n
    else:
        return -1
