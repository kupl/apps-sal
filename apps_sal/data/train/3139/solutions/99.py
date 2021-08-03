def index(array, n=-1):
    if n < 0 or n > len(array) - 1 or n == None:
        val = -1
        return val
    elif n <= len(array) - 1:
        val = array[n]
        val = val ** n
        return val
