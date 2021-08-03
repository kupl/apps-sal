def index(array, n):
    if n < len(array):
        return int(array[n]**n)
    if n >= len(array):
        return -1
