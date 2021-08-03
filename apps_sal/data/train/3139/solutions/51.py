def index(array, n):
    if len(array) < n + 1:
        return -1
    elif len(array) >= n + 1:
        number = array[abs(n)]
        return number ** n
    else:
        pass
