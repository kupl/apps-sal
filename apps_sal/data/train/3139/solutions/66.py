def index(array, n):
    try:
        if len(array) >= n:
            return array[n] ** n
        else:
            return -1
    except IndexError:
        return -1
