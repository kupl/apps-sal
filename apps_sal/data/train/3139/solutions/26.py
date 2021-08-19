def index(array, n):
    if n <= len(array) - 1:
        array[n] = array[n] ** n
        return array[n]
    else:
        return -1
