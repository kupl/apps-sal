def index(array, n):
    for (idx, i) in enumerate(array):
        if idx == n:
            x = array[idx] ** n
            return x
    else:
        return -1
