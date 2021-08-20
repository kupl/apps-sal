def index(array, n):
    print(array)
    print(n)
    if n >= len(array):
        return -1
    else:
        return array[n] ** n
