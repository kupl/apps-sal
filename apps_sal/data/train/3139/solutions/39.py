def index(array, n):
    if len(array) <= n:
        return -1
    for i in range(len(array)):
        if i == n:
            return array[i] ** n
