def index(array, n):
    try:
        if n:
            index = array[n]
            return index ** n
        elif n == 0:
            return 1
    except:
        return -1
