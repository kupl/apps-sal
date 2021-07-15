def index(array, n):
    
    try:
        if (n - 1) > len(array):
            return -1
        else:
            return array[n] ** n

    except IndexError:
        return -1
