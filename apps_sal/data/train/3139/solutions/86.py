def index(array, n):
    arr = len(array)
    if n >= arr:
        return -1
    return array[n]**n
