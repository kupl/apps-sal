def index(array, n):
    if len(array) - 1 < n:
        otvet = -1
    else:
        otvet = array[n]**n
    return otvet
