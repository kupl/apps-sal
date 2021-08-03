def index(array, n):
    try:
        return pow(array[n], n)
    except IndexError:
        return -1
