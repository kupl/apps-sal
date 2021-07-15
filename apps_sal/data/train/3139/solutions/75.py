def index(array, n):
    length = len(array)
    if n <= length - 1:
        return array[n]**n
    else:
        return -1
