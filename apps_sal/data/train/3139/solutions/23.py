def index(array, n):
    for idx in range(len(array)):
        if idx == n:
            return array[idx] ** n
    return -1
