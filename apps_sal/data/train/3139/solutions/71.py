def index(array, n):
    if len(array) > n:
        nTh = array[n] ** n
    else:
        nTh = -1
    return nTh
