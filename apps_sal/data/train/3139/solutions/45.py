def index(array, n=0):
    if n > len(array) - 1:
        return -1
    else:
        return array[n]**n
