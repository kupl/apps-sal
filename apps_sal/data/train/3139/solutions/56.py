def index(array, n):
    list(array)
    if n > len(array) - 1:
        return -1
    else:
        return (array[n]**n)
