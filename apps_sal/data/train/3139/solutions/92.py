def index(array, n):
    if n >= len(array):
        return -1
    print(array, n,"", array[n], "", array[n]**2)
    return array[n]**n
